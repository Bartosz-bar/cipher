import pytest
from src.cipher import Cipher
from src.models import RotType, TextStatus

class TestCipher:

    def setup_method(self) -> None:
        self.cipher = Cipher()

    def test_encrypt_rot13_returns_correct_text(self) -> None:
        result = self.cipher.encrypt("hello", RotType.ROT13)
        assert result.text == "uryyb"

    def test_encrypt_rot13_returns_encrypted_text(self) -> None:
        result = self.cipher.encrypt("hello", RotType.ROT13)
        assert result.status == TextStatus.ENCRYPTED

    def test_decrypt_rot13_returns_original_text(self) -> None:
        result = self.cipher.decrypt("uryyb", RotType.ROT13)
        assert result.text == "hello"

    def test_decrypt_rot13_returns_decrypted_status(self) -> None:
        result = self.cipher.decrypt("uryyb", RotType.ROT13)
        assert result.status == TextStatus.DECRYPTED

    def test_rot13_is_symmetric(self) -> None:
        encrypted = self.cipher.encrypt("hello",RotType.ROT13)
        decrypted = self.cipher.decrypt(encrypted.text, RotType.ROT13)
        assert decrypted.text == "hello"

    def test_rot47_is_symmetric(self) -> None:
        encrypted = self.cipher.encrypt("hello!",RotType.ROT47)
        decrypted = self.cipher.decrypt(encrypted.text, RotType.ROT47)
        assert decrypted.text == "hello!"

    def test_encrypt_rot13_ignores_non_alpha(self) -> None:
        result = self.cipher.encrypt("hello 123!", RotType.ROT13)
        assert result.text == "uryyb 123!"