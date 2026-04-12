from markdownpal.blocks.base import Block


class H1Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"# {self.text}"


class H2Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"## {self.text}"


class H3Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"### {self.text}"


class H4Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"#### {self.text}"


class H5Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"##### {self.text}"


class H6Block(Block):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return f"###### {self.text}"
