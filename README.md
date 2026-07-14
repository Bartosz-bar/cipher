# Cipher

A Python application for encrypting and decrypting text using ROT13 and ROT47 ciphers.

## Features

- ROT13 and ROT47 encryption and decryption
- Buffer system for storing operations during runtime
- JSON file support for saving and loading encrypted/decrypted text
- Interactive menu with match/case handling

## Project Structure

cipher/
├── run.py
├── README.md
├── src/
│   ├── init.py
│   ├── models.py
│   ├── cipher.py
│   ├── buffer.py
│   ├── file_handler.py
│   ├── cipher_facade.py
│   └── manager.py
└── tests/
├── init.py
├── test_cipher.py
├── test_buffer.py
└── test_file_handler.py

## Requirements

- Python 3.11+
- pytest

## Installation

```bash
git clone https://github.com/Bartosz-bar/cipher.git
cd cipher
python -m venv .venv
.venv\Scripts\activate
pip install pytest
```

## Usage

```bash
python run.py
```

## Running Tests

```bash
pytest -v
```

## Design Patterns

- **Facade** — `CipherFacade` connects all subsystems and exposes a simple interface to `Manager`
- **Strategy** — `Rot13Cipher` and `Rot47Cipher` inherit from abstract class `Cipher(ABC)`, each implementing the algorithm independently
- **Dependency Injection** — `Manager` creates concrete cipher objects and injects them into `CipherFacade` via constructor

## Tech Stack

- Python 3.11
- dataclasses
- pytest
