from src.models import Text

class Buffer:
    def __init__(self) -> None:
        self.items: list[Text] = []

    def add(self, item: Text) -> None:
        self.items.append(item)

    def get_all(self) -> list[Text]:
        return self.items

    def clear(self) -> None:
        self.items.clear()

    def is_empty(self) -> bool:
        return len(self.items) == 0