from kalgory.component import BaseBlock
from typing import Tuple

class Block(BaseBlock):
    def handle(key: str, y: int) -> Tuple[str, int]:
        return "HEl123lo"
