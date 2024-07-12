from abc import ABC
import json
from kalgory.bindings.block import Block


class BaseBlock(ABC, Block):
    def execute(self, payload: bytes) -> bytes:
        user_class = self._find_block_class()
        ins = user_class()
        try:
            jsondata = json.loads(payload)
            if len(jsondata) != ins.handle.__code__.co_argcount:
                raise ValueError(f'Block "{user_class.__name__}" 
                                 expects {ins.handle__code__.co_argcount} arguments, but received
                                {ins.handle__code__.co_argcount} arguments from previous blocks')
        except json.JSONDecodeError as je:
            print("JSONDecodeError:", je)
        except ValueError as error:
            print(f"Incoherent between input data and output data: {error}")
        block_output = ins.handle(**jsondata)
        j_dict = []
        for index, data in enumerate(block_output):
            key = f"o{index}"
            j_dict[key] = data
        return json.dumps(j_dict).encode("utf-8")
        

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
