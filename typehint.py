from dataclasses import dataclass
from typing import *


def f(x: int, y: Optional[int] = None) -> int:
    if y is None:
        y = 20
    return x + y


def g(x: Sequence[int]) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()


def l(x: List[str]) -> None:
    print(len(x))
    print(x[0])
    for i in x:
        print(i)
    print()


class Point1(NamedTuple):
    x: int
    y: int = 1  # Set default value


@dataclass
class Point2:
    x: int
    y: int = 1  # Set default value


if __name__ == "__main__":
    print(f(20))
    # g('abcd')  --> error
    g([1, 2, 3])
    # l(('a','b')) --> error
    l(["a", "b"])
    Point1(1)
    Point2(1)

