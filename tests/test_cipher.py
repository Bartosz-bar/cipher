from src.cipher import Rot13Cipher, Rot47Cipher


class TestRot13Cipher:
    def setup_method(self) -> None:
        self.cipher = Rot13Cipher()

    def test_encrypt_returns_correct_text(self) -> None:
        assert self.cipher.encrypt("hello") == "uryyb"

    def test_decrypt_returns_original_text(self) -> None:
        assert self.cipher.decrypt("uryyb") == "hello"

    def test_is_symmetric(self) -> None:
        encrypted = self.cipher.encrypt("hello")
        decrypted = self.cipher.decrypt(encrypted)
        assert decrypted == "hello"

    def test_ignore_non_alpha(self) -> None:
        assert self.cipher.encrypt("hello 123!") == "uryyb 123!"


class TestRot47Cipher:
    def setup_method(self) -> None:
        self.cipher = Rot47Cipher()

    def test_is_symmetric(self) -> None:
        encrypted = self.cipher.encrypt("hello!")
        decrypted = self.cipher.decrypt(encrypted)
        assert decrypted == "hello!"
