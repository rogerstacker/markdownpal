from markdownpal.blocks.base import Block


class TableBlock(Block):
    def __init__(self, headers: list, rows: list) -> None:
        self.headers = headers
        self.rows = rows

    def render(self) -> str:
        header_row = "| " + " | ".join(self.headers) + " |"
        separator = "| " + " | ".join("---" for _ in self.headers) + " |"
        data_rows = [
            "| " + " | ".join(row) + " |"
            for row in self.rows
        ]
        return "\n".join([header_row, separator] + data_rows)
