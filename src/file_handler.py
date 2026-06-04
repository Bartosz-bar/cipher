import json
from pathlib import Path
from src.models import Text, RotType, TextStatus

class FileHandler:

    def save(self, filename:str, items: list[Text]) -> None:
        path = Path(filename)
        existing = []

        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                existing = json.load(f)

        new_items = [self._serialize(item) for item in items]
        existing.extend(new_items)

        with open(path, "w", encoding="utf-8") as f:
                json.dump(existing, f, indent=2, ensure_ascii=False)

    def load(self, filename: str) -> list[Text]:
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(f"File '{filename}' does not exist.")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [self._deserialize(item) for item in data]

    def _serialize(self, item: Text) -> dict:
        return {
            "text": item.text,
            "rot_type": item.rot_type.value,
            "status": item.status.value,
        }

    def _deserialize(self, data: dict) -> Text:
        return Text(
            text=data["text"],
            rot_type=RotType(data["rot_type"]),
            status=TextStatus(data["status"]),
        )