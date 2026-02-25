from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLCDNumber, 
                             QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
                             QLineEdit, QGroupBox, QFormLayout, QSpinBox, 
                             QDoubleSpinBox, QTextEdit, QRadioButton)
from PyQt5.QtCore import Qt, pyqtSlot
from models.calculator_model import CalculatorMode
from controllers.calculator_controller import CalculatorController


class CalculatorView(QWidget):
    def __init__(self, controller: CalculatorController, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Basic", "Scientific", "Finance", "Programming"])
        self.mode_combo.currentIndexChanged.connect(self.on_mode_changed)
        main_layout.addWidget(self.mode_combo)

        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            QLineEdit {
                font-size: 36px;
                padding: 10px;
                border: 2px solid #444;
                border-radius: 5px;
                background-color: #1e1e1e;
                color: white;
            }
        """)
        main_layout.addWidget(self.display)

        self.memory_label = QLabel("M: 0")
        main_layout.addWidget(self.memory_label)

        self.stacked_widget = QWidget()
        self.stacked_layout = QVBoxLayout(self.stacked_widget)

        self.basic_widget = self.create_basic_calculator()
        self.scientific_widget = self.create_scientific_calculator()
        self.finance_widget = self.create_finance_calculator()
        self.programming_widget = self.create_programming_calculator()

        self.stacked_layout.addWidget(self.basic_widget)
        self.stacked_layout.addWidget(self.scientific_widget)
        self.stacked_layout.addWidget(self.finance_widget)
        self.stacked_layout.addWidget(self.programming_widget)

        main_layout.addWidget(self.stacked_widget)

        self.show_basic()

    def show_basic(self):
        self.basic_widget.show()
        self.scientific_widget.hide()
        self.finance_widget.hide()
        self.programming_widget.hide()

    def show_scientific(self):
        self.basic_widget.hide()
        self.scientific_widget.show()
        self.finance_widget.hide()
        self.programming_widget.hide()

    def show_finance(self):
        self.basic_widget.hide()
        self.scientific_widget.hide()
        self.finance_widget.show()
        self.programming_widget.hide()

    def show_programming(self):
        self.basic_widget.hide()
        self.scientific_widget.hide()
        self.finance_widget.hide()
        self.programming_widget.show()

    def create_basic_calculator(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout(widget)

        buttons = [
            ('C', 0, 0), ('CE', 0, 1), ('⌫', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('+/-', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setMinimumHeight(50)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    background-color: #3c3c3c;
                    color: white;
                    border: 1px solid #555;
                    border-radius: 3px;
                }
                QPushButton:hover { background-color: #555; }
                QPushButton:pressed { background-color: #666; }
            """)
            if text in ('=', '+', '-', '*', '/'):
                btn.setStyleSheet("""
                    QPushButton {
                        font-size: 18px;
                        background-color: #ff9500;
                        color: white;
                        border: 1px solid #cc7700;
                        border-radius: 3px;
                    }
                    QPushButton:hover { background-color: #ffaa33; }
                """)
            if text in ('C', 'CE', '⌫'):
                btn.setStyleSheet("""
                    QPushButton {
                        font-size: 18px;
                        background-color: #666;
                        color: white;
                        border: 1px solid #444;
                        border-radius: 3px;
                    }
                    QPushButton:hover { background-color: #777; }
                """)
            btn.clicked.connect(lambda checked, t=text: self.on_basic_button_clicked(t))
            layout.addWidget(btn, row, col)

        memory_layout = QHBoxLayout()
        for text in ['MC', 'MR', 'M+', 'M-']:
            btn = QPushButton(text)
            btn.setMaximumWidth(60)
            btn.clicked.connect(lambda checked, t=text: self.on_memory_button_clicked(t))
            memory_layout.addWidget(btn)
        layout.addLayout(memory_layout, 5, 0, 1, 4)

        return widget

    def create_scientific_calculator(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout(widget)

        self.sci_display = QLineEdit("0")
        self.sci_display.setReadOnly(True)
        self.sci_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sci_display.setStyleSheet("""
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                border: 2px solid #444;
                border-radius: 5px;
                background-color: #1e1e1e;
                color: white;
            }
        """)
        layout.addWidget(self.sci_display, 0, 0, 1, 6)

        angle_group = QGroupBox("Angle")
        angle_layout = QHBoxLayout()
        self.deg_radio = QRadioButton("Degrees")
        self.rad_radio = QRadioButton("Radians")
        self.deg_radio.setChecked(True)
        angle_layout.addWidget(self.deg_radio)
        angle_layout.addWidget(self.rad_radio)
        angle_group.setLayout(angle_layout)
        layout.addWidget(angle_group, 1, 0, 1, 6)

        scientific_buttons = [
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('log', 2, 3), ('ln', 2, 4), ('^', 2, 5),
            ('asin', 3, 0), ('acos', 3, 1), ('atan', 3, 2), ('exp', 3, 3), ('n!', 3, 4), ('1/x', 3, 5),
            ('π', 4, 0), ('e', 4, 1), ('(', 4, 2), (')', 4, 3), ('√', 4, 4), ('%', 4, 5),
            ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('4', 6, 0), ('5', 6, 1), ('6', 6, 2),
            ('/', 5, 3), ('*', 5, 4), ('-', 5, 5),
            ('1', 7, 0), ('2', 7, 1), ('3', 7, 2), ('+', 6, 3), ('=', 6, 4), ('C', 6, 5),
            ('0', 8, 0), ('.', 8, 1), ('⌫', 8, 2),
        ]

        for text, row, col in scientific_buttons:
            btn = QPushButton(text)
            btn.setMinimumHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 14px;
                    background-color: #3c3c3c;
                    color: white;
                    border: 1px solid #555;
                    border-radius: 3px;
                }
                QPushButton:hover { background-color: #555; }
            """)
            if text in ('sin', 'cos', 'tan', 'log', 'ln', 'exp', 'asin', 'acos', 'atan', 'n!', '1/x', '√', '%', '^'):
                btn.setStyleSheet("""
                    QPushButton {
                        font-size: 14px;
                        background-color: #555;
                        color: white;
                        border: 1px solid #444;
                        border-radius: 3px;
                    }
                    QPushButton:hover { background-color: #666; }
                """)
            btn.clicked.connect(lambda checked, t=text: self.on_scientific_button_clicked(t))
            layout.addWidget(btn, row, col)

        return widget

    def create_finance_calculator(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        calc_type_group = QGroupBox("Calculation Type")
        calc_type_layout = QVBoxLayout()

        self.finance_calc_combo = QComboBox()
        self.finance_calc_combo.addItems([
            "Compound Interest",
            "Present Value",
            "Future Value",
            "Loan Payment",
            "ROI",
            "CAGR",
            "Straight Line Depreciation",
            "Double Declining Depreciation",
            "Tip Calculator"
        ])
        self.finance_calc_combo.currentIndexChanged.connect(self.on_finance_type_changed)
        calc_type_layout.addWidget(self.finance_calc_combo)
        calc_type_group.setLayout(calc_type_layout)
        layout.addWidget(calc_type_group)

        self.finance_inputs = QFormLayout()
        self.finance_param1 = QDoubleSpinBox()
        self.finance_param2 = QDoubleSpinBox()
        self.finance_param3 = QDoubleSpinBox()
        self.finance_param4 = QDoubleSpinBox()
        
        for sp in [self.finance_param1, self.finance_param2, self.finance_param3, self.finance_param4]:
            sp.setRange(-999999999, 999999999)
            sp.setDecimals(2)
            
        self.finance_label1 = QLabel("Parameter 1:")
        self.finance_label2 = QLabel("Parameter 2:")
        self.finance_label3 = QLabel("Parameter 3:")
        self.finance_label4 = QLabel("Parameter 4:")
            
        self.finance_inputs.addRow(self.finance_label1, self.finance_param1)
        self.finance_inputs.addRow(self.finance_label2, self.finance_param2)
        self.finance_inputs.addRow(self.finance_label3, self.finance_param3)
        self.finance_inputs.addRow(self.finance_label4, self.finance_param4)
        layout.addLayout(self.finance_inputs)

        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.on_finance_calculate)
        calc_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                background-color: #ff9500;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #ffaa33; }
        """)
        layout.addWidget(calc_btn)

        self.finance_result = QLabel("Result: 0")
        self.finance_result.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.finance_result)

        layout.addStretch()

        self.update_finance_labels()
        return widget

    def create_programming_calculator(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        base_group = QGroupBox("Number Base")
        base_layout = QHBoxLayout()

        self.base_combo = QComboBox()
        self.base_combo.addItems(["BIN", "OCT", "DEC", "HEX"])
        self.base_combo.currentIndexChanged.connect(self.on_base_changed)
        base_layout.addWidget(self.base_combo)
        base_group.setLayout(base_layout)
        layout.addWidget(base_group)

        convert_group = QGroupBox("Base Conversion")
        convert_layout = QGridLayout()

        self.prog_display = QLineEdit("0")
        self.prog_display.setStyleSheet("font-size: 20px; padding: 5px;")
        convert_layout.addWidget(QLabel("Value:"), 0, 0)
        convert_layout.addWidget(self.prog_display, 0, 1, 1, 2)

        convert_buttons = [
            ("To Binary", 1, 0), ("To Octal", 1, 1), ("To Hex", 1, 2),
            ("From Binary", 2, 0), ("From Octal", 2, 1), ("From Hex", 2, 2),
        ]
        
        for text, row, col in convert_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, t=text: self.on_conversion_clicked(t))
            convert_layout.addWidget(btn, row, col)
            
        convert_group.setLayout(convert_layout)
        layout.addWidget(convert_group)

        bitwise_group = QGroupBox("Bitwise Operations")
        bitwise_layout = QGridLayout()

        self.bitwise_a = QLineEdit()
        self.bitwise_a.setPlaceholderText("Value A")
        self.bitwise_b = QLineEdit()
        self.bitwise_b.setPlaceholderText("Value B")
        bitwise_layout.addWidget(QLabel("A:"), 0, 0)
        bitwise_layout.addWidget(self.bitwise_a, 0, 1)
        bitwise_layout.addWidget(QLabel("B:"), 1, 0)
        bitwise_layout.addWidget(self.bitwise_b, 1, 1)

        bitwise_ops = [("AND", 0, 2), ("OR", 0, 3), ("XOR", 1, 2), ("<<", 0, 4), (">>", 1, 4)]
        for text, row, col in bitwise_ops:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, t=text: self.on_bitwise_clicked(t))
            bitwise_layout.addWidget(btn, row, col)

        self.bitwise_result = QLabel("Result: 0")
        self.bitwise_result.setStyleSheet("font-size: 18px; font-weight: bold;")
        bitwise_layout.addWidget(self.bitwise_result, 2, 0, 1, 5)

        bitwise_group.setLayout(bitwise_layout)
        layout.addWidget(bitwise_group)

        return widget

    @pyqtSlot(int)
    def on_mode_changed(self, index):
        modes = [CalculatorMode.BASIC, CalculatorMode.SCIENTIFIC, CalculatorMode.FINANCE, CalculatorMode.PROGRAMMING]
        self.controller.set_mode(modes[index])
        
        if index == 0:
            self.show_basic()
        elif index == 1:
            self.show_scientific()
        elif index == 2:
            self.show_finance()
        elif index == 3:
            self.show_programming()

    @pyqtSlot(str)
    def on_basic_button_clicked(self, text):
        if text.isdigit() or text == '.':
            if text == '.':
                self.controller.input_decimal()
            else:
                self.controller.input_digit(text)
        elif text in ('+', '-', '*', '/', '%', '^'):
            self.controller.input_operation(text)
        elif text == '=':
            self.controller.input_equal()
        elif text == 'C':
            self.controller.input_clear()
        elif text == 'CE':
            self.controller.input_clear_all()
        elif text == '⌫':
            self.controller.input_backspace()
        elif text == '+/-':
            self.controller.input_plus_minus()

    @pyqtSlot(str)
    def on_memory_button_clicked(self, text):
        if text == 'MC':
            self.controller.memory_clear()
        elif text == 'MR':
            self.controller.memory_recall()
        elif text == 'M+':
            self.controller.memory_add()
        elif text == 'M-':
            self.controller.memory_subtract()

    @pyqtSlot(str)
    def on_scientific_button_clicked(self, text):
        if text == 'C':
            self.controller.input_clear()
        elif text == '⌫':
            self.controller.input_backspace()
        elif text == '=':
            self.controller.input_equal()
        elif text in ('sin', 'cos', 'tan', 'log', 'ln', 'exp', 'asin', 'acos', 'atan', 'n!', '1/x', '√', '%'):
            self.controller.input_operation(text)
        elif text == 'π':
            self.controller.input_digit(str(3.141592653589793))
        elif text == 'e':
            self.controller.input_digit(str(2.718281828459045))
        elif text in ('(', ')'):
            self.controller.input_digit(text)
        elif text == '^':
            self.controller.input_operation('^')
        elif text.isdigit() or text == '.':
            if text == '.':
                self.controller.input_decimal()
            else:
                self.controller.input_digit(text)

    def update_finance_labels(self):
        calc_type = self.finance_calc_combo.currentText()
        labels = {
            "Compound Interest": ("Principal:", "Rate (%):", "Time (years):", "Compounds/yr:"),
            "Present Value": ("Future Value:", "Rate (%):", "Time (years):", ""),
            "Future Value": ("Present Value:", "Rate (%):", "Time (years):", ""),
            "Loan Payment": ("Principal:", "Rate (%):", "Years:", ""),
            "ROI": ("Initial Investment:", "Final Value:", "", ""),
            "CAGR": ("Start Value:", "End Value:", "Periods (years):", ""),
            "Straight Line Depreciation": ("Cost:", "Salvage Value:", "Life (years):", ""),
            "Double Declining Depreciation": ("Cost:", "Life (years):", "Period:", ""),
            "Tip Calculator": ("Bill Amount:", "Tip (%):", "Number of People:", ""),
        }
        
        params = labels.get(calc_type, ("Param 1:", "Param 2:", "Param 3:", "Param 4:"))
        
        self.finance_label1.setText(params[0] if len(params) > 0 else "Param 1:")
        self.finance_label2.setText(params[1] if len(params) > 1 else "Param 2:")
        self.finance_label3.setText(params[2] if len(params) > 2 else "Param 3:")
        self.finance_label4.setText(params[3] if len(params) > 3 else "Param 4:")
        
        self.finance_param4.setVisible(len(params) > 3 and params[3] != "")

    @pyqtSlot(int)
    def on_finance_type_changed(self, index):
        self.update_finance_labels()

    def on_finance_calculate(self):
        calc_type = self.finance_calc_combo.currentText()
        p1 = self.finance_param1.value()
        p2 = self.finance_param2.value()
        p3 = self.finance_param3.value()
        p4 = self.finance_param4.value()

        calc_map = {
            "Compound Interest": ("compound_interest", {'principal': p1, 'rate': p2, 'time': p3, 'n': int(p4) if p4 else 12}),
            "Present Value": ("present_value", {'future_value': p1, 'rate': p2, 'time': p3}),
            "Future Value": ("future_value", {'present_value': p1, 'rate': p2, 'time': p3}),
            "Loan Payment": ("payment", {'principal': p1, 'rate': p2, 'n_periods': int(p3 * 12)}),
            "ROI": ("roi", {'initial': p1, 'final': p2}),
            "CAGR": ("cagr", {'start': p1, 'end': p2, 'periods': p3}),
            "Straight Line Depreciation": ("depreciation_sl", {'cost': p1, 'salvage': p2, 'life': p3}),
            "Double Declining Depreciation": ("depreciation_ddb", {'cost': p1, 'life': p2, 'period': int(p3)}),
            "Tip Calculator": ("tip", {'bill': p1, 'tip_percent': p2, 'num_people': int(p3) if p3 else 1}),
        }

        calc_key, params = calc_map.get(calc_type, ("", {}))
        result = self.controller.finance_calculation(calc_key, params)
        
        if result is not None:
            self.finance_result.setText(f"Result: {result:.4f}")
        else:
            self.finance_result.setText("Result: Error")

    @pyqtSlot(int)
    def on_base_changed(self, index):
        bases = [2, 8, 10, 16]
        self.controller._programming.set_base(bases[index])

    @pyqtSlot(str)
    def on_conversion_clicked(self, text):
        value = self.prog_display.text()
        
        conversion_map = {
            "To Binary": "to_binary",
            "To Octal": "to_octal", 
            "To Hex": "to_hex",
            "From Binary": "from_binary",
            "From Octal": "from_octal",
            "From Hex": "from_hex",
        }
        
        result = self.controller.programming_conversion(conversion_map[text], value)
        if result:
            self.prog_display.setText(result)

    @pyqtSlot(str)
    def on_bitwise_clicked(self, text):
        try:
            a = int(self.bitwise_a.text(), 0)
            b = int(self.bitwise_b.text(), 0)
        except ValueError:
            self.bitwise_result.setText("Result: Invalid input")
            return

        ops = {
            "AND": lambda: a & b,
            "OR": lambda: a | b,
            "XOR": lambda: a ^ b,
            "<<": lambda: a << b,
            ">>": lambda: a >> b,
        }

        result = ops.get(text, lambda: 0)()
        self.bitwise_result.setText(f"Result: {result} (0x{result:X})")

    def update_display(self, value: str):
        self.display.setText(value)

    def update_memory(self, value: float):
        self.memory_label.setText(f"M: {value}")
