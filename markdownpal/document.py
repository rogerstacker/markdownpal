from markdownpal.blocks.base import Block


class Document:
    def __init__(self) -> None:
        self._blocks: list[Block] = []

    def append(self, block: Block) -> None:
        if not isinstance(block, Block):
            raise TypeError(f"Expected a Block instance, got {type(block).__name__}")
        self._blocks.append(block)

    def render(self) -> str:
        return "\n\n".join(block.render() for block in self._blocks)

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
