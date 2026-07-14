from src.cipher import Cipher, Rot13Cipher, Rot47Cipher
from src.models import RotType


class CipherFactory:
    _registry: dict[RotType, type[Cipher]] = {
        RotType.ROT13: Rot13Cipher,
        RotType.ROT47: Rot47Cipher,
    }

    @classmethod
    def create(cls, rot_type: RotType) -> Cipher:
        cipher_cls = cls._registry.get(rot_type)

        if cipher_cls is None:
            raise ValueError(f"Unknown cipher type: {rot_type}")

        return cipher_cls()

    @classmethod
    def create_all(cls) -> dict[RotType, Cipher]:
        return {rot_type: cls.create(rot_type) for rot_type in cls._registry}
