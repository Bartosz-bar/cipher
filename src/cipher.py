from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def _rotate(self, text: str) -> str:
        pass


class Rot13Cipher(Cipher):
    def _rotate(self, text: str) -> str:
        result = []

        for char in text:
            if "a" <= char <= "z":
                result.append(chr((ord(char) - ord("a") + 13) % 26 + ord("a")))
            elif "A" <= char <= "Z":
                result.append(chr((ord(char) - ord("A") + 13) % 26 + ord("A")))
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, text: str) -> str:
        return self._rotate(text)

    def decrypt(self, text: str) -> str:
        return self._rotate(text)


class Rot47Cipher(Cipher):
    def _rotate(self, text: str) -> str:
        result = []

        for char in text:
            if "!" <= char <= "~":
                result.append(chr((ord(char) - ord("!") + 47) % 94 + ord("!")))
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, text: str) -> str:
        return self._rotate(text)

    def decrypt(self, text: str) -> str:
        return self._rotate(text)
