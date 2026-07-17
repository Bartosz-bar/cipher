import pytest

from src.cipher_facade import CipherFacade
from src.models import RotType, Text


@pytest.fixture
def facade(mocker):
    mock_cipher = mocker.patch("src.cipher.Rot13Cipher")
    mock_buffer = mocker.patch("src.buffer.Buffer")
    mock_file_handler = mocker.patch("src.file_handler.FileHandler")

    return CipherFacade(
        ciphers={RotType.ROT13: mock_cipher},
        buffer=mock_buffer,
        file_handler=mock_file_handler,
    )


def test_encrypt_calls_cipher_encrypt(facade) -> None:
    facade._ciphers[RotType.ROT13].encrypt.return_value = "uryyb"
    facade.encrypt("hello", RotType.ROT13)
    facade._ciphers[RotType.ROT13].encrypt.assert_called_once_with("hello")


def test_encrypt_adds_result_to_buffer(facade) -> None:
    facade._ciphers[RotType.ROT13].encrypt.return_value = "uryyb"
    facade.encrypt("hello", RotType.ROT13)
    facade._buffer.add.assert_called_once()


def test_decrypt_calls_cipher_decrypt(facade) -> None:
    facade._ciphers[RotType.ROT13].decrypt.return_value = "hello"
    facade.decrypt("uryyb", RotType.ROT13)
    facade._ciphers[RotType.ROT13].decrypt.assert_called_once_with("uryyb")


def test_save_to_file_raises_when_buffer_empty(facade) -> None:
    facade._buffer.is_empty.return_value = True
    with pytest.raises(ValueError):
        facade.save_to_file("output.json")


def test_load_from_file_adds_items_to_buffer(facade, mocker) -> None:
    mock_item = mocker.MagicMock(spec=Text)
    facade._file_handler.load.return_value = [mock_item]
    facade.load_from_file("input.json")
    facade._buffer.add.assert_called_once_with(mock_item)
