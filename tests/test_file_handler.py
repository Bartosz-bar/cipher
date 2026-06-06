import pytest
from src.file_handler import FileHandler
from src.cipher import Cipher
from src.models import RotType, TextStatus

class TestFileHandler:

    def setup_method(self) -> None:
        self.file_handler = FileHandler()
        self.cipher = Cipher()

    def test_save_creates_file(self, tmp_path) -> None:
        items = [self.cipher.encrypt("hello",RotType.ROT13),]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        assert (tmp_path / "test.json").exists()

    def test_save_and_load_returns_same_text(self, tmp_path) -> None:
        items = [self.cipher.encrypt("hello",RotType.ROT13),]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].text == "uryyb"

    def test_save_and_load_returns_correct_rot_type(self, tmp_path) -> None:
        items = [self.cipher.encrypt("hello",RotType.ROT13),]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].rot_type == RotType.ROT13

    def test_save_and_load_returns_correct_status(self, tmp_path) -> None:
        items = [self.cipher.encrypt("hello",RotType.ROT13),]
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, items)
        loaded = self.file_handler.load(filepath)
        assert loaded[0].status == TextStatus.ENCRYPTED

    def test_save_appends_to_exisiting_file(self, tmp_path) -> None:
        filepath = str(tmp_path / "test.json")
        self.file_handler.save(filepath, [self.cipher.encrypt("hello",RotType.ROT13),])
        self.file_handler.save(filepath, [self.cipher.encrypt("world",RotType.ROT47),])
        loaded = self.file_handler.load(filepath)
        assert len(loaded) == 2

    def test_load_raises_error_when_file_not_found(self) -> None:
        with pytest.raises(FileNotFoundError):
            self.file_handler.load("nonexistent.json")