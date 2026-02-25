import math
from typing import Union, Optional


class ArithmeticOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> Optional[float]:
        if b == 0:
            return None
        return a / b

    @staticmethod
    def modulo(a: float, b: float) -> Optional[float]:
        if b == 0:
            return None
        return a % b

    @staticmethod
    def power(a: float, b: float) -> float:
        return math.pow(a, b)

    @staticmethod
    def square_root(a: float) -> Optional[float]:
        if a < 0:
            return None
        return math.sqrt(a)

    @staticmethod
    def percentage(value: float, percent: float) -> float:
        return (value * percent) / 100

    @staticmethod
    def negate(a: float) -> float:
        return -a

    @staticmethod
    def reciprocal(a: float) -> Optional[float]:
        if a == 0:
            return None
        return 1 / a

    @staticmethod
    def factorial(n: int) -> Optional[int]:
        if n < 0:
            return None
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def absolute(a: float) -> float:
        return abs(a)

    @staticmethod
    def evaluate(expression: str) -> Optional[float]:
        try:
            allowed_names = {
                'sqrt': math.sqrt,
                'pow': math.pow,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log10,
                'ln': math.log,
                'exp': math.exp,
                'pi': math.pi,
                'e': math.e,
                'factorial': math.factorial,
                'abs': abs,
            }
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return float(result) if result is not None else None
        except Exception:
            return None
