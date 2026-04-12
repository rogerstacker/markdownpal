from markdownpal.blocks.base import Block


class CodeBlock(Block):
    def __init__(self, code: str, lang: str = "") -> None:
        self.code = code
        self.lang = lang

    def render(self) -> str:
        return f"```{self.lang}\n{self.code}\n```"
