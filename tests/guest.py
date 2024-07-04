from kalgory import BaseBlock


class CustomBlock(BaseBlock):
    def handle(self, key: str, y: int) -> str:
        return f"{key}: {y}"
