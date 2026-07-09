from src.buffer import Buffer
from src.cipher000 import Cipher
from src.models import RotType, TextStatus

class TestBuffer:

    def setup_method(self) -> None:
        self.buffer = Buffer()
        self.cipher = Cipher()

    def test_buffer_is_empty_on_start(self) -> None:
        assert self.buffer.is_empty() is True

    def test_buffer_is_not_empty_after_add(self) -> None:
        item = self.cipher.encrypt("hello",RotType.ROT13)
        self.buffer.add(item)
        assert self.buffer.is_empty() is False

    def test_buffer_get_all_returns_added_items(self) -> None:
        item = self.cipher.encrypt("hello",RotType.ROT13)
        self.buffer.add(item)
        assert len(self.buffer.get_all()) == 1

    def test_buffer_get_all_returns_correct_items(self) -> None:
        item = self.cipher.encrypt("hello",RotType.ROT13)
        self.buffer.add(item)
        assert self.buffer.get_all()[0].text == "uryyb"

    def test_buffer_clear_empties_buffer(self) -> None:
        self.buffer.add(self.cipher.encrypt("hello",RotType.ROT13))
        self.buffer.clear()
        assert self.buffer.is_empty() is True

    def test_buffer_stores_multiple_items(self) -> None:
        self.buffer.add(self.cipher.encrypt("hello",RotType.ROT13))
        self.buffer.add(self.cipher.encrypt("world",RotType.ROT47))
        assert len(self.buffer.get_all()) == 2

    def test_buffer_stores_all_items(self) -> None:
        item = self.cipher.encrypt("hello",RotType.ROT13)
        self.buffer.add(item)
        assert self.buffer.get_all()[0].status == TextStatus.ENCRYPTED