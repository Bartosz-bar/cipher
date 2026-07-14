import pytest

from src.cipher import Rot13Cipher, Rot47Cipher
from src.file_handler import FileHandler
from src.models import RotType, Text, TextStatus


class TestFileHandler:
    def setup_method(self) -> None:
        self.file_handler = FileHandler()
        self.rot13 = Rot13Cipher()
        self.rot47 = Rot47Cipher()

    def _encrypt(self, text: str, rot_type: RotType) -> Text:
        cipher = self.rot13 if rot_type == RotType.ROT13 else self.rot47
        encrypted = cipher.encrypt(text)
        return Text(text=encrypted, rot_type=rot_type, status=TextStatus.ENCRYPTED)

    def test_save_creates_file(self, tmp_path) -> None:
        items = [self._encrypt("hello", RotType.ROT13)]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        assert (tmp_path / "test.json").exists()

    def test_save_and_load_returns_same_text(self, tmp_path) -> None:
        items = [self._encrypt("hello", RotType.ROT13)]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].text == "uryyb"

    def test_save_and_load_returns_correct_rot_type(self, tmp_path) -> None:
        items = [self._encrypt("hello", RotType.ROT13)]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].rot_type == RotType.ROT13

    def test_save_and_load_returns_correct_status(self, tmp_path) -> None:
        items = [self._encrypt("hello", RotType.ROT13)]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].status == TextStatus.ENCRYPTED

    def test_save_appends_to_existing_file(self, tmp_path) -> None:
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, [self._encrypt("hello", RotType.ROT13)])
        self.file_handler.save(filepath, [self._encrypt("world", RotType.ROT47)])
        loaded = self.file_handler.load(filepath)
        assert len(loaded) == 2

    def test_load_raises_error_when_file_not_found(self) -> None:
        with pytest.raises(FileNotFoundError):
            self.file_handler.load("nonexistent.json")
