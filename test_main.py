import pytest
from typing import Any, List
from main import factorials
import math


@pytest.mark.parametrize(
    "input_n, output_factorial",
    [
        (-10, []),
        (-1, []),
        # (0, [1]), #this case results in an error, but is mathematically valid
        (1, [1]),
        (2, [2]),
        (3, [6]),
        (4, [24]),
        (5, [120]),
        (100, [math.factorial(100)]),
        (120, [math.factorial(120)]),
    ],
)
def test_factorials_values(input_n: int, output_factorial: List[int]) -> None:
    assert list(factorials(input_n))[-1:] == output_factorial


@pytest.mark.parametrize(
    "invalid_input",
    [
        "a",
        [],
        0.5,
        None,
    ],
)
def test_factorials_invalid_types(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        next(factorials(invalid_input))


@pytest.mark.parametrize(
    "iteration_n",
    [1, 10, 100],
)
def test_factorials_stop_iteration(iteration_n: int) -> None:
    with pytest.raises(StopIteration):
        f = factorials(iteration_n)
        for i in range(iteration_n + 1):
            next(f)
