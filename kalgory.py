"""Python client library for kalgory, a visualization and drag n' drop tool for algorithmic trader"""
__version__ = "0.1.0-dev"

from abc import ABC

from bindings.block import Block


class BaseBlock(ABC, Block):
    def execute(self, payload: bytes) -> bytes:
        return payload

    def _find_block_class(self) -> type:
        classes = self.__class__.__subclasses__()
        if len(classes) == 0:
            raise RuntimeError("BaseBlock should be implemented as Block")
        elif len(classes) > 1:
            raise RuntimeError("Multiple BaseBlock classes found: {[classes.__name__ for cls in classes]}")
        elif classes[0].__name__ != "Block":
            raise RuntimeError("The block should be named as Block")
        else:
            return classes[0]
