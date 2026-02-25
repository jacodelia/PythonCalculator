from typing import Optional
from PyQt5.QtCore import QObject, pyqtSignal
from models.calculator_model import CalculatorModel, CalculatorMode
from operations import ArithmeticOperations, ScientificOperations, FinanceOperations, ProgrammingOperations


class CalculatorController(QObject):
    display_changed = pyqtSignal(str)
    mode_changed = pyqtSignal(str)
    memory_changed = pyqtSignal(float)
    error_occurred = pyqtSignal(str)

    def __init__(self, model: Optional[CalculatorModel] = None):
        super().__init__()
        self._model = model if model else CalculatorModel()
        self._arithmetic = ArithmeticOperations()
        self._scientific = ScientificOperations()
        self._finance = FinanceOperations()
        self._programming = ProgrammingOperations()

    @property
    def model(self):
        return self._model

    def get_display_text(self) -> str:
        return self._model.get_display_value()

    def get_mode(self) -> CalculatorMode:
        return self._model.get_mode()

    def set_mode(self, mode: CalculatorMode):
        self._model.set_mode(mode)
        self.mode_changed.emit(mode.value)
        self.display_changed.emit(self._model.get_display_value())

    def input_digit(self, digit: str):
        self._model.append_digit(digit)
        self.display_changed.emit(self._model.get_display_value())

    def input_decimal(self):
        current = self._model.get_display_value()
        if '.' not in current:
            if current == "":
                self._model.set_display_value("0.")
            else:
                self._model.set_display_value(current + ".")
        self.display_changed.emit(self._model.get_display_value())

    def input_operation(self, operation: str):
        if operation in ('+', '-', '*', '/', '%', '^'):
            self._model.set_pending_operation(operation)
        else:
            result = self._model.apply_unary_operation(operation)
            if result is not None:
                self.display_changed.emit(self._model.get_display_value())
            else:
                self.error_occurred.emit("Invalid operation")

    def input_equal(self):
        result = self._model.calculate()
        if result is not None:
            self.display_changed.emit(self._model.get_display_value())
        else:
            self.error_occurred.emit("Calculation error")

    def input_clear(self):
        self._model.clear()
        self.display_changed.emit(self._model.get_display_value())

    def input_clear_all(self):
        self._model.clear_all()
        self.display_changed.emit(self._model.get_display_value())
        self.memory_changed.emit(self._model.get_memory())

    def input_backspace(self):
        current = self._model.get_display_value()
        if len(current) > 1:
            self._model.set_display_value(current[:-1])
        else:
            self._model.set_display_value("0")
        self.display_changed.emit(self._model.get_display_value())

    def input_plus_minus(self):
        self.input_operation("+/-")

    def memory_add(self):
        self._model.memory_add()
        self.memory_changed.emit(self._model.get_memory())

    def memory_subtract(self):
        self._model.memory_subtract()
        self.memory_changed.emit(self._model.get_memory())

    def memory_recall(self):
        self._model.memory_recall()
        self.display_changed.emit(self._model.get_display_value())

    def memory_clear(self):
        self._model.memory_clear()
        self.memory_changed.emit(self._model.get_memory())

    def get_history(self) -> list:
        return self._model.get_history()

    def get_memory(self) -> float:
        return self._model.get_memory()

    def set_angle_mode_degrees(self, use_degrees: bool):
        self._model.angle_mode_degrees = use_degrees

    def get_angle_mode_degrees(self) -> bool:
        return self._model.angle_mode_degrees

    def evaluate_expression(self, expression: str) -> Optional[float]:
        result = self._arithmetic.evaluate(expression)
        if result is not None:
            self._model.set_display_value(str(result))
            self.display_changed.emit(self._model.get_display_value())
        else:
            self.error_occurred.emit("Invalid expression")
        return result

    def finance_calculation(self, calc_type: str, params: dict) -> Optional[float]:
        result = None
        try:
            if calc_type == "compound_interest":
                result = self._finance.compound_interest(
                    params.get('principal', 0),
                    params.get('rate', 0),
                    params.get('time', 0),
                    params.get('n', 12)
                )
            elif calc_type == "present_value":
                result = self._finance.present_value(
                    params.get('future_value', 0),
                    params.get('rate', 0),
                    params.get('time', 0)
                )
            elif calc_type == "future_value":
                result = self._finance.future_value(
                    params.get('present_value', 0),
                    params.get('rate', 0),
                    params.get('time', 0)
                )
            elif calc_type == "payment":
                result = self._finance.payment(
                    params.get('principal', 0),
                    params.get('rate', 0),
                    params.get('n_periods', 0)
                )
            elif calc_type == "roi":
                result = self._finance.roi(
                    params.get('initial', 0),
                    params.get('final', 0)
                )
            elif calc_type == "cagr":
                result = self._finance.cagr(
                    params.get('start', 0),
                    params.get('end', 0),
                    params.get('periods', 0)
                )
            elif calc_type == "depreciation_sl":
                result = self._finance.depreciation_straight_line(
                    params.get('cost', 0),
                    params.get('salvage', 0),
                    params.get('life', 0)
                )
            elif calc_type == "depreciation_ddb":
                result = self._finance.depreciation_double_declining_balance(
                    params.get('cost', 0),
                    params.get('life', 0),
                    params.get('period', 0)
                )
            elif calc_type == "tip":
                result = self._finance.tip_calculator(
                    params.get('bill', 0),
                    params.get('tip_percent', 0),
                    params.get('num_people', 1)
                )
            
            if result is not None:
                self._model.set_display_value(str(result))
                self.display_changed.emit(self._model.get_display_value())
            else:
                self.error_occurred.emit("Finance calculation error")
                
        except Exception as e:
            self.error_occurred.emit(str(e))
            
        return result

    def programming_conversion(self, conversion_type: str, value: str) -> Optional[str]:
        result = None
        try:
            if conversion_type == "to_binary":
                result = self._programming.to_binary(value, 10)
            elif conversion_type == "to_octal":
                result = self._programming.to_octal(value, 10)
            elif conversion_type == "to_hex":
                result = self._programming.to_hexadecimal(value, 10)
            elif conversion_type == "from_binary":
                result = str(self._programming.to_decimal(value, 2))
            elif conversion_type == "from_octal":
                result = str(self._programming.to_decimal(value, 8))
            elif conversion_type == "from_hex":
                result = str(self._programming.to_decimal(value, 16))

            if result is not None:
                self._model.set_display_value(result)
                self.display_changed.emit(self._model.get_display_value())
            else:
                self.error_occurred.emit("Conversion error")
                
        except Exception as e:
            self.error_occurred.emit(str(e))
            
        return result
