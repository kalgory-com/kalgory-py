import subprocess

import pytest
from wasmtime import Store


class TestBlock:
    @pytest.fixture
    def compile_block(self, tmp_path):
        path = f"{tmp_path}/block.wasm"
        subprocess.run([
            "componentize-py",
            "-d", "./wit",
            "-w", "kalgory:block/block@0.1.0",
            "componentize", "-s", "tests.guest", "-o", path,
        ])
        yield path

    @pytest.fixture
    def generate_bindings(self, compile_block):
        subprocess.run([
            "python3", "-m",
            "wasmtime.bindgen", compile_block,
            "--out-dir", "tests/bindings"
        ])

    def test_execute(self, generate_bindings):
        with Store() as store:
            from tests.bindings import Root
            component = Root(store)
            assert component.execute(store, bytes(range(10))).value == "Block".encode("utf-8")
