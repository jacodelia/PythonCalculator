from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from views.calculator_view import CalculatorView
from controllers.calculator_controller import CalculatorController
from models.calculator_model import CalculatorModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setMinimumSize(400, 600)
        
        self.model = CalculatorModel()
        self.controller = CalculatorController(self.model)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        self.calculator_view = CalculatorView(self.controller)
        layout.addWidget(self.calculator_view)
        
        self.controller.display_changed.connect(self.calculator_view.update_display)
        self.controller.memory_changed.connect(self.calculator_view.update_memory)
        self.controller.error_occurred.connect(self.show_error)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QWidget {
                color: white;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: white;
            }
            QGroupBox {
                color: white;
                border: 1px solid #555;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QComboBox {
                background-color: #3c3c3c;
                color: white;
                border: 1px solid #555;
                padding: 5px;
                border-radius: 3px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #2c2c2c;
                color: white;
                selection-background-color: #555;
            }
            QLineEdit {
                background-color: #3c3c3c;
                color: white;
                border: 1px solid #555;
                border-radius: 3px;
                padding: 5px;
            }
            QSpinBox, QDoubleSpinBox {
                background-color: #3c3c3c;
                color: white;
                border: 1px solid #555;
                border-radius: 3px;
                padding: 5px;
            }
            QSpinBox::up-button, QDoubleSpinBox::up-button,
            QSpinBox::down-button, QDoubleSpinBox::down-button {
                background-color: #555;
            }
            QRadioButton {
                color: white;
            }
            QRadioButton::indicator {
                background-color: #3c3c3c;
            }
        """)

    def show_error(self, message: str):
        QMessageBox.warning(self, "Error", message)
