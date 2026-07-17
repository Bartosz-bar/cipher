import pytest

from src.cipher import Rot13Cipher, Rot47Cipher
from src.cipher_factory import CipherFactory
from src.models import RotType


class TestCipherFactory:
    def test_create_returns_rot13_cipher(self) -> None:
        cipher = CipherFactory.create(RotType.ROT13)
        assert isinstance(cipher, Rot13Cipher)

    def test_create_returns_rot47_cipher(self) -> None:
        cipher = CipherFactory.create(RotType.ROT47)
        assert isinstance(cipher, Rot47Cipher)

    def test_create_all_returns_all_cipher_types(self) -> None:
        ciphers = CipherFactory.create_all()
        assert RotType.ROT13 in ciphers
        assert RotType.ROT47 in ciphers

    def test_create_all_returns_correct_instances(self) -> None:
        ciphers = CipherFactory.create_all()
        assert isinstance(ciphers[RotType.ROT13], Rot13Cipher)
        assert isinstance(ciphers[RotType.ROT47], Rot47Cipher)

    def test_create_raises_for_unknown_type(self) -> None:
        with pytest.raises(ValueError):
            CipherFactory.create("unknown")
