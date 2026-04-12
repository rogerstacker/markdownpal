from markdownpal.blocks.base import Block


class TextBlock(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return self.text


class QuoteBlock(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return "\n".join(f"> {line}" for line in self.text.splitlines())


class HRBlock(Block):
    def render(self) -> str:
        return "---"


class CommentBlock(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"<!-- {self.text} -->"
