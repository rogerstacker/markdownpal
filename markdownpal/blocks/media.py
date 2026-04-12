from markdownpal.blocks.base import Block


class ImageBlock(Block):
    def __init__(self, src: str, alt: str = "") -> None:
        self.src = src
        self.alt = alt

    def render(self) -> str:
        return f"![{self.alt}]({self.src})"


class LinkBlock(Block):
    def __init__(self, text: str, url: str) -> None:
        self.text = text
        self.url = url

    def render(self) -> str:
        return f"[{self.text}]({self.url})"
