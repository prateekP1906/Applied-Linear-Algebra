import math
import random
import sys
from typing import Self

class Vec:
    def __init__ (self, src=None) -> Self: 
        if src is None:
            self.elements = ()
        else :
            elements = tuple(src)
            for x in elements:
                if not isinstance (x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __sub__ (self, t: Self) -> Self:
        if not isinstance(t, Vec): 
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Vectors must be the same dimensions")

        return Vec([round(x-y, 5) for x, y in zip(self.elements, t.elements)])

    def __add__ (self, t: Self) -> Self:
        if not isinstance(t, Vec): 
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Vectors must be the same dimensions")
        return Vec([round(x+y, 5) for x, y in zip(self.elements, t.elements)])

    def __rmul__ (self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(t)}")

        return Vec([round(x * scalar, 5) for x in self.elements])
    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        self.elements = [round(val * scalar, 5) for val in self.elements]
        return self

    def __repr__ (self)-> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements])

    def __radd__(self, other: int | float) -> Self:
        if not isinstance(other, (int, float)):
            raise TypeError(f"Can only add a number to a vector, got {type(other)}")
        return Vec([round(x + other, 5) for x in self.elements])

    def __iadd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")
        
        if len(self.elements) != len(other.elements):
            raise TypeError(f"Vectors must be same in Dimension")

        self.elements = [round(x + y, 5) for x, y in zip(self.elements, other.elements)]
        return self
    
    @staticmethod
    def zeros(n: int) -> Self:
        if n <= 0:
            raise ValueError(f"Dimension n must be positive (>0)")
        return Vec([0.0] * n)
    
    @staticmethod
    def ones(n: int) -> Self:
        if n <= 0:
            raise ValueError(f"Dimension n must be positive (>0)")
        return Vec([1.0] * n)

    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError(f"Dimension n must be positive (>0)")
        return Vec([random.random() for _ in range(n)])
    
    def norm(self) -> float:
        return math.sqrt(sum(x ** 2 for x in self.elements))

    if sys.version_info < (3, 8):
        sys.exit(f"Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":

    v1 = Vec([0, 1, 1.03])
    print(v1)
    v3 = 2.2 * v1
    print(v3)
    v3 *= 5
    print(v3)
    v2 = v1 + v3
    print(v1 + v3)

