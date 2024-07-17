# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# ----

# Copyright (c) Fermyon Technologies. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import json
import subprocess

import pytest
from wasmtime import Store


class TestBlock:
    @pytest.fixture
    def compile_block(self, tmp_path):
        path = f"{tmp_path}/block.wasm"
        subprocess.run(
            [
                "componentize-py",
                "-d",
                "wit",
                "-w",
                "kalgory:component/block@0.1.0",
                "componentize",
                "-s",
                "tests.guest",
                "-o",
                path,
            ]
        )
        yield path

    @pytest.fixture
    def generate_bindings(self, compile_block):
        subprocess.run(["python3", "-m", "wasmtime.bindgen", compile_block, "--out-dir", "tests/bindings"])

    def test_execute(self, generate_bindings):
        with Store() as store:
            from tests.bindings import Root

            data = [1, 20010714.0, (123, "fefe")]
            out = [20010715, (123, "fefe")]
            data = json.dumps(data).encode("utf-8")
            out = json.dumps(out).encode("utf-8")
            component = Root(store)
            assert component.execute(store, data).value == out

    def test_pure_execution(self):
        from tests.guest import Block

        block = Block()
        data = [1, 20010714.0, (123, "fefe")]
        out = [20010715, (123, "fefe")]
        data = json.dumps(data).encode("utf-8")
        out = json.dumps(out).encode("utf-8")

        assert block.execute(data) == out
