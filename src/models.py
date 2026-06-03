from dataclasses import dataclass
from enum import Enum

class RotType(Enum):
    ROT13 = "rot13"
    ROT47 = "rot47"

class TextStatus(Enum):
    ENCRYPTED = "encrypted"
    DECRYPTED = "decrypted"

@dataclass
class Text:
    text: str
    rot_type: RotType
    status: TextStatus