"""
__init__.py

This file tells Python that the "my_utils" folder is a package.

We also import some functions here so they can be used directly like this:
    from my_utils import reverse_string, add

Instead of writing the longer version:
    from my_utils.string_utils import reverse_string
    from my_utils.math_utils import add

Both ways work. This file just makes the shorter way possible.
"""

from .string_utils import reverse_string
from .math_utils import add
