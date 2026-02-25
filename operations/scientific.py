import math
import cmath
import random
from typing import Union, Optional, Tuple


class ScientificOperations:
    @staticmethod
    def sin(angle: float, degrees: bool = True) -> float:
        if degrees:
            angle = math.radians(angle)
        return math.sin(angle)

    @staticmethod
    def cos(angle: float, degrees: bool = True) -> float:
        if degrees:
            angle = math.radians(angle)
        return math.cos(angle)

    @staticmethod
    def tan(angle: float, degrees: bool = True) -> Optional[float]:
        if degrees:
            angle = math.radians(angle)
        try:
            return math.tan(angle)
        except:
            return None

    @staticmethod
    def asin(value: float, degrees: bool = True) -> Optional[float]:
        if abs(value) > 1:
            return None
        result = math.asin(value)
        return math.degrees(result) if degrees else result

    @staticmethod
    def acos(value: float, degrees: bool = True) -> Optional[float]:
        if abs(value) > 1:
            return None
        result = math.acos(value)
        return math.degrees(result) if degrees else result

    @staticmethod
    def atan(value: float, degrees: bool = True) -> float:
        result = math.atan(value)
        return math.degrees(result) if degrees else result

    @staticmethod
    def sinh(x: float) -> float:
        return math.sinh(x)

    @staticmethod
    def cosh(x: float) -> float:
        return math.cosh(x)

    @staticmethod
    def tanh(x: float) -> float:
        return math.tanh(x)

    @staticmethod
    def log(x: float, base: float = 10) -> Optional[float]:
        if x <= 0:
            return None
        if base == 10:
            return math.log10(x)
        elif base == math.e:
            return math.log(x)
        else:
            return math.log(x) / math.log(base)

    @staticmethod
    def ln(x: float) -> Optional[float]:
        if x <= 0:
            return None
        return math.log(x)

    @staticmethod
    def exp(x: float) -> float:
        return math.exp(x)

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    @staticmethod
    def nth_root(x: float, n: float) -> Optional[float]:
        if x < 0 and n % 2 == 0:
            return None
        if x == 0:
            return 0
        if x < 0:
            return -math.pow(-x, 1 / n)
        return math.pow(x, 1 / n)

    @staticmethod
    def cube_root(x: float) -> float:
        if x >= 0:
            return math.pow(x, 1/3)
        else:
            return -math.pow(-x, 1/3)

    @staticmethod
    def factorial(n: int) -> Optional[int]:
        if n < 0:
            return None
        return math.factorial(n)

    @staticmethod
    def combinations(n: int, r: int) -> Optional[int]:
        if n < 0 or r < 0 or r > n:
            return None
        return math.comb(n, r)

    @staticmethod
    def permutations(n: int, r: int) -> Optional[int]:
        if n < 0 or r < 0 or r > n:
            return None
        return math.perm(n, r)

    @staticmethod
    def gamma(x: float) -> Optional[float]:
        if x <= 0 and x == int(x):
            return None
        try:
            return math.gamma(x)
        except:
            return None

    @staticmethod
    def log_gamma(x: float) -> Optional[float]:
        if x <= 0:
            return None
        try:
            return math.lgamma(x)
        except:
            return None

    @staticmethod
    def sqrt(x: float) -> Optional[float]:
        if x < 0:
            return None
        return math.sqrt(x)

    @staticmethod
    def abs(x: float) -> float:
        return abs(x)

    @staticmethod
    def ceil(x: float) -> float:
        return math.ceil(x)

    @staticmethod
    def floor(x: float) -> float:
        return math.floor(x)

    @staticmethod
    def round(x: float) -> float:
        return round(x)

    @staticmethod
    def random() -> float:
        return random.random()

    @staticmethod
    def randint(min_val: int, max_val: int) -> int:
        return random.randint(min_val, max_val)

    @staticmethod
    def prime_factorization(n: int) -> Optional[list]:
        if n <= 0:
            return None
        factors = []
        d = 2
        temp = n
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        return factors

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def gcd(a: int, b: int) -> int:
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def complex_add(a: complex, b: complex) -> complex:
        return a + b

    @staticmethod
    def complex_subtract(a: complex, b: complex) -> complex:
        return a - b

    @staticmethod
    def complex_multiply(a: complex, b: complex) -> complex:
        return a * b

    @staticmethod
    def complex_divide(a: complex, b: complex) -> Optional[complex]:
        if b == 0:
            return None
        return a / b

    @staticmethod
    def complex_magnitude(c: complex) -> float:
        return abs(c)

    @staticmethod
    def complex_phase(c: complex) -> float:
        return cmath.phase(c)

    @staticmethod
    def complex_conjugate(c: complex) -> complex:
        return c.conjugate()

    @staticmethod
    def complex_polar(c: complex) -> Tuple[float, float]:
        return cmath.polar(c)

    @staticmethod
    def complex_rect(r: float, theta: float) -> complex:
        return cmath.rect(r, math.radians(theta))

    @staticmethod
    def to_scientific_notation(x: float, precision: int = 10) -> str:
        return f"{x:.{precision}e}"

    @staticmethod
    def from_scientific_notation(s: str) -> Optional[float]:
        try:
            return float(s)
        except:
            return None
