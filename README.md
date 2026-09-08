# my_utils

A small Python package I made with simple helper functions for
working with strings and numbers.

## What it does

`my_utils` has two parts:

- `string_utils.py` – functions for text (reverse text, count vowels, capitalize words).
- `math_utils.py` – functions for basic math (add, subtract, multiply, divide).

## Project structure

```
my_utils/
├── __init__.py
├── string_utils.py
└── math_utils.py

driver.py
```

## How to import it

Make sure `driver.py` (or your own script) is in the same folder
as the `my_utils` folder. Then you can import functions like this:

```python
from my_utils.string_utils import reverse_string
from my_utils.math_utils import add
```

Or, since `__init__.py` already imports a couple of them, you can also do:

```python
from my_utils import reverse_string, add
```

## How to use it

```python
from my_utils.string_utils import reverse_string
from my_utils.math_utils import add

print(reverse_string("hello"))   # olleh
print(add(2, 3))                 # 5
```

## Running the demo

Run the driver script to see all the functions in action:

```
python driver.py
```
