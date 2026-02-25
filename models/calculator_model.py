from enum import Enum
from typing import Optional, Any
from operations import ArithmeticOperations, ScientificOperations, FinanceOperations, ProgrammingOperations


class CalculatorMode(Enum):
    BASIC = "basic"
    SCIENTIFIC = "scientific"
    FINANCE = "finance"
    PROGRAMMING = "programming"


class CalculatorModel:
    def __init__(self):
        self.mode = CalculatorMode.BASIC
        self.display_value = "0"
        self.pending_operation = None
        self.first_operand = None
        self.should_clear_display = False
        self.history = []
        self.memory = 0
        self.angle_mode_degrees = True

        self.arithmetic = ArithmeticOperations()
        self.scientific = ScientificOperations()
        self.finance = FinanceOperations()
        self.programming = ProgrammingOperations()

    def set_mode(self, mode: CalculatorMode):
        self.mode = mode
        self.clear()

    def get_mode(self) -> CalculatorMode:
        return self.mode

    def set_display_value(self, value: str):
        self.display_value = value

    def get_display_value(self) -> str:
        if self.pending_operation and self.first_operand is not None:
            return f"{self.first_operand} {self.pending_operation}"
        return self.display_value

    def clear(self):
        self.display_value = "0"
        self.pending_operation = None
        self.first_operand = None
        self.should_clear_display = False

    def clear_all(self):
        self.clear()
        self.memory = 0

    def append_digit(self, digit: str):
        if self.should_clear_display:
            self.display_value = ""
            self.should_clear_display = False

        if self.display_value == "0" and digit != ".":
            self.display_value = digit
        else:
            self.display_value += digit

    def set_pending_operation(self, operation: str):
        if self.first_operand is None:
            self.first_operand = float(self.display_value)
        else:
            self.calculate()

        self.pending_operation = operation
        self.should_clear_display = True

    def calculate(self) -> Optional[float]:
        if self.pending_operation is None or self.first_operand is None:
            return None

        try:
            second_operand = float(self.display_value)
            result = self._execute_operation(self.first_operand, second_operand, self.pending_operation)

            if result is not None:
                self.history.append(f"{self.first_operand} {self.pending_operation} {second_operand} = {result}")
                self.display_value = str(result)
                self.first_operand = result
                self.pending_operation = None
                self.should_clear_display = True

            return result
        except Exception:
            self.display_value = "Error"
            return None

    def _execute_operation(self, a: float, b: float, operation: str) -> Optional[float]:
        if self.mode == CalculatorMode.BASIC:
            return self._arithmetic_operation(a, b, operation)
        elif self.mode == CalculatorMode.SCIENTIFIC:
            return self._scientific_operation(a, b, operation)
        elif self.mode == CalculatorMode.PROGRAMMING:
            return self._programming_operation(a, b, operation)
        return None

    def _arithmetic_operation(self, a: float, b: float, operation: str) -> Optional[float]:
        operations = {
            '+': lambda: self.arithmetic.add(a, b),
            '-': lambda: self.arithmetic.subtract(a, b),
            '*': lambda: self.arithmetic.multiply(a, b),
            '/': lambda: self.arithmetic.divide(a, b),
            '%': lambda: self.arithmetic.modulo(a, b),
            '^': lambda: self.arithmetic.power(a, b),
        }
        return operations.get(operation, lambda: None)()

    def _scientific_operation(self, a: float, b: float, operation: str) -> Optional[float]:
        operations = {
            '+': lambda: self.arithmetic.add(a, b),
            '-': lambda: self.arithmetic.subtract(a, b),
            '*': lambda: self.arithmetic.multiply(a, b),
            '/': lambda: self.arithmetic.divide(a, b),
            '%': lambda: self.arithmetic.modulo(a, b),
            '^': lambda: self.scientific.power(a, b),
            'nth_root': lambda: self.scientific.nth_root(a, b),
        }
        return operations.get(operation, lambda: None)()

    def _programming_operation(self, a: float, b: float, operation: str) -> Optional[int]:
        int_a = int(a)
        int_b = int(b)
        operations = {
            'AND': lambda: self.programming.bitwise_and(int_a, int_b),
            'OR': lambda: self.programming.bitwise_or(int_a, int_b),
            'XOR': lambda: self.programming.bitwise_xor(int_a, int_b),
            '<<': lambda: self.programming.left_shift(int_a, int_b),
            '>>': lambda: self.programming.right_shift(int_a, int_b),
        }
        return operations.get(operation, lambda: None)()

    def apply_unary_operation(self, operation: str) -> Optional[float]:
        try:
            value = float(self.display_value)
        except ValueError:
            return None

        if self.mode == CalculatorMode.BASIC or self.mode == CalculatorMode.SCIENTIFIC:
            result = self._apply_unary(value, operation)
            if result is not None:
                self.display_value = str(result)
            return result
        return None

    def _apply_unary(self, value: float, operation: str) -> Optional[float]:
        if operation == "+/-":
            return self.arithmetic.negate(value)
        elif operation == "1/x":
            return self.arithmetic.reciprocal(value)
        elif operation == "sqrt":
            return self.arithmetic.square_root(value)
        elif operation == "sin":
            return self.scientific.sin(value, self.angle_mode_degrees)
        elif operation == "cos":
            return self.scientific.cos(value, self.angle_mode_degrees)
        elif operation == "tan":
            return self.scientific.tan(value, self.angle_mode_degrees)
        elif operation == "log":
            return self.scientific.log(value)
        elif operation == "ln":
            return self.scientific.ln(value)
        elif operation == "exp":
            return self.scientific.exp(value)
        elif operation == "factorial":
            return self.scientific.factorial(int(value))
        elif operation == "abs":
            return self.scientific.abs(value)
        elif operation == "floor":
            return self.scientific.floor(value)
        elif operation == "ceil":
            return self.scientific.ceil(value)
        return None

    def memory_add(self):
        try:
            self.memory += float(self.display_value)
        except ValueError:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.display_value)
        except ValueError:
            pass

    def memory_recall(self):
        self.display_value = str(self.memory)

    def memory_clear(self):
        self.memory = 0

    def get_history(self) -> list:
        return self.history

    def get_memory(self) -> float:
        return self.memory
