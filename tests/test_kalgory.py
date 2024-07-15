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
            data = {"o1": 1, "o2": 20010714., "o3": (123, "fefe")}
            out = {"o1": 20010715, "o2":(123, "fefe")}
            data = json.dumps(data).encode("utf-8") 
            out = json.dumps(out).encode("utf-8") 
            component = Root(store)
            assert component.execute(store, data).value == out

    def test_pure_execution(self):
        from tests.guest import Block
        block = Block()
        data = {"o1": 1, "o2": 20010714., "o3": (123, "fefe")}
        out = {"o1": 20010715, "o2":(123, "fefe")}
        data = json.dumps(data).encode("utf-8")
        out = json.dumps(out).encode("utf-8") 

        assert block.execute(data) == out
