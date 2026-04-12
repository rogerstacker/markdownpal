from markdownpal.blocks.base import Block


class MarkdownDocument:
    def __init__(self) -> None:
        self._blocks: list = []

    def append(self, block: Block) -> None:
        self._blocks.append(block)

    def render(self) -> str:
        return "\n\n".join(block.render() for block in self._blocks)

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
