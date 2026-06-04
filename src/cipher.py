from src.models import Text, RotType, TextStatus

class Cipher:

    def encrypt(self, text: str, rot_type: RotType) -> Text:
        encrypted = self._rotate(text, rot_type)
        return Text(text=encrypted, rot_type=rot_type, status=TextStatus.ENCRYPTED)

    def decrypt(self, text: str, rot_type: RotType) -> Text:
        decrypted = self._rotate(text, rot_type)
        return Text(text=decrypted, rot_type=rot_type, status=TextStatus.DECRYPTED)

    def _rotate(self, text: str, rot_type: RotType) -> str:
        if rot_type == RotType.ROT13:
            return self._rot13(text)
        return self._rot47(text)

    def _rot13(self, text: str) -> str:
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    def _rot47(self, text: str) -> str:
        result = []

        for char in text:
            if '!' <= char <= '~':
                result.append(chr((ord(char) - ord('!') + 47) % 94 + ord('!')))
            else:
                result.append(char)
            return ''.join(result)