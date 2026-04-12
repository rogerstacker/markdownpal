from markdownpal.blocks.base import Block


class ULBlock(Block):
    def __init__(self, items: list) -> None:
        self.items = items

    def render(self) -> str:
        return "\n".join(f"- {item}" for item in self.items)


class OLBlock(Block):
    def __init__(self, items: list) -> None:
        self.items = items

    def render(self) -> str:
        return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(self.items))


class TaskListBlock(Block):
    def __init__(self, items: list) -> None:
        # items: list of (text, done) tuples
        self.items = items

    def render(self) -> str:
        lines = []
        for text, done in self.items:
            checkbox = "x" if done else " "
            lines.append(f"- [{checkbox}] {text}")
        return "\n".join(lines)
