import subprocess

import pytest


class TestBlock:
    @pytest.fixture
    def compile_block(self, tmp_path):
        path = f"{tmp_path}/block.wasm"
        subprocess.run([
            "componentize-py",
            "-d", "./wit",
            "-w", "kalgory:block/block@0.1.0",
            "componentize", "tests.guest", "-o", path,
        ])
        yield path

    def test_find_block_class(self, compile_block):
        pass
