# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from abc import ABC

from kalgory.bindings.block import Block

from .utility import validate, zipjson


class BaseBlock(ABC, Block):
    def execute(self, payload: bytes) -> bytes:
        user_class = self._find_block_class()
        ins = user_class()

        # JSON deserizlie
        try:
            jsondata = json.loads(payload)
        except json.JSONDecodeError as je:
            raise RuntimeError(f"Exception caught: {je}") from je
        validate(ins, jsondata)
        block_output = ins.handle(*jsondata)

        j_dict = zipjson(block_output)
        return j_dict

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
