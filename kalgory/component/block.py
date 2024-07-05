from abc import ABC

from kalgory.bindings.block import Block


class BaseBlock(ABC, Block):
    def execute(self, payload: bytes) -> bytes:
        return self._find_block_class().__name__.encode('utf-8')

    @staticmethod
    def _find_block_class() -> type:
        classes = BaseBlock.__subclasses__()
        if len(classes) == 0:
            raise RuntimeError("BaseBlock should be implemented as Block")
        elif len(classes) > 1:
            raise RuntimeError("Multiple BaseBlock classes found: {[classes.__name__ for cls in classes]}")
        elif classes[0].__name__ != "Block":
            raise RuntimeError("The block should be named as Block")
        else:
            return classes[0]
