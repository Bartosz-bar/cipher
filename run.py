from src.buffer import Buffer
from src.file_handler import FileHandler
from src.manager import Manager


def main() -> None:
    manager = Manager(buffer=Buffer(), file_handler=FileHandler())
    manager.run()


if __name__ == "__main__":
    main()
