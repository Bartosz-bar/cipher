from src.buffer import Buffer
from src.cipher import Cipher
from src.file_handler import FileHandler
from src.models import RotType, Text, TextStatus


class CipherFacade:
    def __init__(
        self, ciphers: dict[RotType, Cipher], buffer: Buffer, file_handler: FileHandler
    ) -> None:
        self._ciphers = ciphers
        self._buffer = buffer
        self._file_handler = file_handler

    def encrypt(self, text: str, rot_type: RotType) -> Text:
        cipher = self._ciphers.get(rot_type)
        encrypted_text = cipher.encrypt(text)
        result = Text(
            text=encrypted_text, rot_type=rot_type, status=TextStatus.ENCRYPTED
        )
        self._buffer.add(result)
        return result

    def decrypt(self, text: str, rot_type: RotType) -> Text:
        cipher = self._ciphers.get(rot_type)
        decrypted_text = cipher.decrypt(text)
        result = Text(
            text=decrypted_text, rot_type=rot_type, status=TextStatus.DECRYPTED
        )
        self._buffer.add(result)
        return result

    def get_buffer(self) -> list[Text]:
        return self._buffer.get_all()

    def clear_buffer(self) -> None:
        self._buffer.clear()

    def is_buffer_empty(self) -> bool:
        return self._buffer.is_empty()

    def save_to_file(self, filename: str) -> None:
        if self._buffer.is_empty():
            raise ValueError("Buffer is empty, nothing to save.")
        self._file_handler.save(filename, self._buffer.get_all())

    def load_from_file(self, filename: str) -> list[Text]:
        items = self._file_handler.load(filename)
        for item in items:
            self._buffer.add(item)
        return items
