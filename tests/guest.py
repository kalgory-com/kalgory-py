from kalgory.component import BaseBlock


class Block(BaseBlock):
    def handle(self, key: str, y: int) -> str:
        return f"{key}: {y}"
