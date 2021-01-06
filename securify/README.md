# securify

A minimal and secure command-line password manager.

## Installation

```shell
pip install securify
```

## Warnings

- This code comes with absolutely no guarantee and is distributed under the WTFPL license.
- First of all make sure that your storage ( the place where the program will store `.vault` is secure )
- All metadata is not encrypted.
- All passwords are encrypted using a 64 character long string ( master key ). The QR code for the master key is generated. Store it in a secure place.
- When you want to perform CRUD, on the database, you will need to make sure that the master key (`master.txt`) is the current directory from where you are running `securify`.
- Thus all security depends on the place you store the vault and master key.
- The code comes with **absolutely no guarantee.**


## Usage


