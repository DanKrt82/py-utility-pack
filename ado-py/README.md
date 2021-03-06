# ado-py

Do stuff with python. Quickly access functions from the command-line.

Automate stuff and save time.

Inspired by make. 😂

To avoid repetition of lines in the terminal, we often create a make alias and call
`make func`

In `make` you write stuff in shell, in `ado`, you write in python.

## Installation

```shell
pip install ado-py
```

## Usage

Create a `do.py` file in your directory.

Write functions in it like this

```python
'''
docstring of do.py
write whatever you want
'''

def hello():
    print('hi')

def func():
    # do stuff here
    pass

```

Note: the functions in `do.py` should not take any arguments.
For user input use `input()` function.

Call any function from the terminal by running `ado func`.

Running only `ado` would print the docstring of `do.py`.


## Alternatives

[Typer CLI](https://typer.tiangolo.com/typer-cli/) is simply great. It also supports auto-completion. 
