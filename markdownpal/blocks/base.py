from abc import ABC, abstractmethod


class Block(ABC):
    @abstractmethod
    def render(self) -> str:
        """Return the Markdown string for this block."""
        ...
