"""Incremental statistics implementation
"""
import sys
import math

from typing import Union, List, Optional
from collections import Counter

Number = Union[int, float]

class Statistics:
    """Class that carries the calculation of basic numerical statistics
    in a accumulative way. In most of the cases, the spatial cost does not grow
    with the amount of the numbers used to calculate the statistics.

    Attributes:
        count (int): Amount of samples
        counter (Counter): Amount of samples per value
        max (Number): Max value
        min (Number): Min value
        sum (Number): Summatory of the values
    """

    def __init__(self):
        """Constructor
        """
        self.counter = Counter()
        self.sum = 0
        self.count = 0
        self.min = sys.maxsize
        self.max = 0

    def add(self, elements: Union[List[Number], Number]):
        """Adds a new value of a list of values

        Args:
            elements (Union[List[Number], Number]): A number or a list of numbers
        """
        if not isinstance(elements, list):
            elements = [elements]

        for value in elements:
            self.counter[value] += 1
            self.sum += value
            self.min = min(value, self.min)
            self.max = max(value, self.max)

        self.count += len(elements)

    def update(self, other: "Statistics"):
        """Aggregates the values of another Statistics object

        Args:
            other (Statistics): The other statistics
        """
        for k, value in other.counter.items():
            self.counter[k] += value
            self.sum += (k * value)
            self.min = min(k, self.min)
            self.max = max(k, self.max)

        self.count += len(other)

    def clear(self):
        """Sets everything to 'zero'
        """
        self.counter.clear()
        self.sum = 0
        self.count = 0
        self.min = sys.maxsize
        self.max = 0

    def mean(self) -> Optional[Number]:
        """Average of the distribution

        Returns:
            Optional[Number]: The average. Returns None if there are no samples.
        """
        if self.count > 0:
            return self.sum / self.count

        return None

    def var(self) -> Optional[Number]:
        """Variance of the distribution

        Returns:
            Optional[Number]: The variance. Returns None if there are no samples.
        """
        if self.count > 0:
            res = 0
            avg = self.sum / self.count

            for k, v in self.counter.items():
                res += ((k - avg)**2) * v

            return res / self.count

        return None

    def std(self) -> Optional[Number]:
        """Standard variation of the distribution

        Returns:
            Optional[Number]: The std. Returns None if there are no samples.
        """
        var = self.var()

        if var is not None:
            return math.sqrt(var)

        return None

    def median(self) -> Optional[Number]:
        """Median of the distribution

        Returns:
            Optional[Number]: The median. Returns None if there are no samples.
        """
        return self.quantile(0.5)

    def quantile(self, q: float) -> Optional[Number]:
        """Quantile of a distribution

        Args:
            q (float): A value from 0 to 1

        Returns:
            Optional[Number]: The q quantile. Returns None when no samples.

        Raises:
            ValueError: Description
        """
        if not 0 <= q <= 1:
            raise ValueError("q must be within the range from 0 to 1")

        if self.count > 0:
            if q == 0:
                return self.min

            if q == 1:
                return self.max

            if q <= 0.5:
                size = (self.count - 1) * q
                size_1 = int((self.count - 1) * q)
                size_2 = math.ceil((self.count - 1) * q)
                items = sorted(self.counter.items(), key=lambda x: x[0])

            else:
                size = (self.count - 1) * (1 - q)
                size_1 = int((self.count - 1) * (1 - q))
                size_2 = math.ceil((self.count - 1) * (1 - q))
                items = sorted(
                    self.counter.items(), key=lambda x: x[0], reverse=True
                )

            count = 0
            a: Optional[Number] = None
            b: Optional[Number] = None

            for k, v in items:
                res = k
                count += v

                if a is None and (count - 1) >= size_1:
                    a = k

                if b is None and (count - 1) >= size_2:
                    b = k

                if a is not None and b is not None:
                    break

            assert a is not None and b is not None
            return a + (size - size_1) * (b - a)

        return None

    def values(self) -> list:
        """Summary

        Returns:
            list: Description
        """
        vals = []

        for k, v in self.counter.items():
            vals.extend([k] * v)

        return vals

    def report(self) -> dict:
        """Returns a dictionary with the statistics

        Returns:
            dict: The statistics. Returns an empty dictionary when no samples.
        """
        if self.count == 0:
            return {}

        return {
            "count": self.count,
            "mean": self.mean(),
            "std": self.std(),
            "var": self.var(),
            "median": self.median(),
            "q1": self.quantile(0.25),
            "q3": self.quantile(0.75),
            "min": self.min,
            "max": self.max
        }

    def __len__(self) -> int:
        """ Return the number of samples

        Returns:
            int: Num of samples
        """
        return self.count

    def __repr__(self) -> str:
        """ Returns the report

        Returns:
            str: the report
        """
        return repr(self.report())

    def __str__(self) -> str:
        """ Returns the report

        Returns:
            str: the report
        """
        return str(self.report())
