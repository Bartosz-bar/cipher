from src.cipher_facade import CipherFacade
from src.cipher_factory import CipherFactory
from src.models import RotType

class Manager:
    def __init__(self, buffer, file_handler) -> None:
        ciphers = CipherFactory.create_all()
        self._facade = CipherFacade(ciphers=ciphers, buffer=buffer, file_handler=file_handler)

    def run(self) -> None:
        print("Welcome to CIPHER!")
        while True:
            self._print_menu()
            choice = input("Choose option: ").strip()

            match choice:
                case "1":
                    self._handle_encrypt()
                case "2":
                    self._handle_decrypt()
                case "3":
                    self._handle_show_buffer()
                case "4":
                    self._handle_save_to_file()
                case "5":
                    self._handle_load_from_file()
                case "6":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid option, try again.")

    def _print_menu(self) -> None:
        print("\n===== MENU =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Show buffer")
        print("4. Save to file")
        print("5. Load from file")
        print("6. Exit")
        print("=================")

    def _get_rot_type(self) -> RotType:
        while True:
            choice = input("Choose ROT type (1 = ROT13, 2 = ROT47): ").strip()
            match choice:
                case "1":
                    return RotType.ROT13
                case "2":
                    return RotType.ROT47
                case _:
                    print("Invalid choice, try again.")

    def _handle_encrypt(self) -> None:
        text = input("Enter text to encrypt: ").strip()
        rot_type = self._get_rot_type()
        result = self._facade.encrypt(text, rot_type)
        print(f"Encrypted: {result.text}")

    def _handle_decrypt(self) -> None:
        text = input("Enter text to decrypt: ").strip()
        rot_type = self._get_rot_type()
        result = self._facade.decrypt(text, rot_type)
        print(f"Decrypted: {result.text}")

    def _handle_show_buffer(self) -> None:
        if self._facade.is_buffer_empty():
            print("Buffer is empty.")
            return
        print("\n===== BUFFER =====")
        for item in self._facade.get_buffer():
            print(f"[{item.status.value}] [{item.rot_type.value}] {item.text}")
        print("==================")

    def _handle_save_to_file(self) -> None:
        try:
            filename = input("Enter filename (e.g. output.json): ").strip()
            self._facade.save_to_file(filename)
            print(f"Saved to {filename}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_load_from_file(self) -> None:
        try:
            filename = input("Enter filename to load: ").strip()
            items = self._facade.load_from_file(filename)
            print(f"Loaded {len(items)} items into buffer.")
        except FileNotFoundError as e:
            print(f"Error: {e}")