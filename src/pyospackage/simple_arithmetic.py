"""A module that performs basic math operations."""

import numpy as np
import numpy.typing as npt


def add_integers(
    a: int,
    b: int,
) -> int:
    """A function that adds two integers together

    Parameters
    ----------
    a : int
        The first integer to be added.
    b : int
        The second integer to be added.

    Returns
    -------
    int
        The sum of the two provided integers.
    """

    if not np.isscalar(a):
        raise TypeError(f"Expected a scalar, got {a}")
    if not isinstance(a, int):
        raise TypeError(f"Expected a integer, got {a}")
    if not np.isscalar(b):
        raise TypeError(f"Expected a scalar, got {b}")
    if not isinstance(b, int):
        raise TypeError(f"Expected a integer, got {b}")

    return a + b


def multiply_integers(
    a: int,
    b: int,
) -> int:
    """A function that multiplies two integers together

    Parameters
    ----------
    a : int
        The first integer to be multiplied.
    b : int
        The second integer to be multiplied.

    Returns
    -------
    int
        The product of the two provided integers.
    """
    if not np.isscalar(a):
        raise TypeError(f"Expected a scalar, got {a}")
    if not isinstance(a, int):
        raise TypeError(f"Expected an integer, got {a}")
    if not np.isscalar(b):
        raise TypeError(f"Expected a scalar, got {b}")
    if not isinstance(b, int):
        raise TypeError(f"Expected an integer, got {b}")

    return a * b


def create_int_vector(
    a: int,
    b: int,
) -> npt.NDArray[np.int32]:
    """Create a numpy 1-D array

    Parameters
    ----------
    a : int
        The length of the 1-D array.
    b : int
        The integer with which to populate the array.

    Returns
    -------
    ndarray[int]
        The sum of the two provided integers.
    """

    if not np.isscalar(a):
        raise TypeError(f"Expected a scalar, got {a}")
    if not isinstance(a, int):
        raise TypeError(f"Expected an integer, got {a}")
    if not np.isscalar(b):
        raise TypeError(f"Expected a scalar, got {b}")
    if not isinstance(b, int):
        raise TypeError(f"Expected an integer, got {b}")

    return np.ones(a, dtype=int) * b
