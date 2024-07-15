from typing import Tuple

from kalgory.component import BaseBlock


class Block(BaseBlock):
    def handle(self, x:int, y:float, z:list[int, str]) -> Tuple[int, str]:
        y = int(y)
        return  (x + y, z)
