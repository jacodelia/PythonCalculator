# Scientific Calculator

A cross-platform desktop calculator application built with Python and PyQt5, following the MVVC (Model-View-ViewModel-Controller) architectural pattern and OOP principles. Inspired by the GNOME Calculator.

## Features

### Basic Calculator
- Arithmetic operations: +, -, *, /, %
- Power (^)
- Square root
- Percentage
- Memory operations (MC, MR, M+, M-)
- Sign toggle (+/-)

### Scientific Calculator
- Trigonometric functions: sin, cos, tan (degrees/radians)
- Inverse trigonometric: asin, acos, atan
- Hyperbolic functions: sinh, cosh, tanh
- Logarithms: log (base 10), ln (natural)
- Exponential: exp
- Factorial (n!)
- Combinatorics: combinations, permutations
- Gamma function
- Prime factorization
- GCD/LCM
- Complex number operations
- Floor/ceiling
- Random number generation

### Finance Calculator
- Compound interest
- Present value (PV)
- Future value (FV)
- Loan payment calculator
- ROI calculator
- CAGR (Compound Annual Growth Rate)
- Straight-line depreciation
- Double-declining depreciation
- Tip calculator

### Programming Calculator
- Base conversion (Binary, Octal, Decimal, Hexadecimal)
- Bitwise operations: AND, OR, XOR
- Bit shifting: <<, >>
- Bit rotation
- Individual bit manipulation
- RGB/Hex color conversion
- ASCII conversions

## Project Structure

```
calculator/
├── main.py                    # Application entry point
├── controllers/
│   ├── __init__.py
│   └── calculator_controller.py  # ViewModel - handles business logic
├── models/
│   ├── __init__.py
│   └── calculator_model.py       # Model - data and state management
├── operations/
│   ├── __init__.py
│   ├── arithmetic.py             # Basic arithmetic operations
│   ├── scientific.py             # Scientific functions
│   ├── finance.py               # Financial calculations
│   └── programming.py           # Binary/bitwise operations
├── views/
│   ├── __init__.py
│   ├── calculator_view.py       # View - UI components
│   └── main_window.py          # Main application window
└── tests/
    └── test_operations.py       # Comprehensive test suite
```

## Architecture (MVVC Pattern)

### Model
- `CalculatorModel`: Manages calculator state, current mode, display value, memory, and history
- Uses `CalculatorMode` enum to switch between Basic, Scientific, Finance, and Programming modes

### View
- `CalculatorView`: PyQt5 widgets for each calculator mode
- `MainWindow`: Main application window with dark theme styling
- Handles user input and displays results

### ViewModel (Controller)
- `CalculatorController`: Bridges Model and View
- Processes user input, executes operations through the Model
- Emits signals for display updates and errors

### Operations (Separate Module)
All mathematical operations are isolated in the `operations/` package for:
- Clean separation of concerns
- Easy testing
- Reusability across different parts of the app

## Requirements

- Python 3.8+
- PyQt5
- pytest (for testing)

## Installation

```bash
# Create a virtual environment (recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Or install individually:

```bash
pip install PyQt5
```

## Usage

### Running the Application

```bash
# With virtual environment activated
python3 main.py
```

### Running Tests

```bash
# Run all tests
pytest tests/test_operations.py -v
```

Or with the virtual environment:

```bash
venv/bin/pytest tests/test_operations.py -v
```

### Run specific test classes

```bash
# Test only arithmetic
pytest tests/test_operations.py::TestArithmeticOperations -v

# Test only scientific
pytest tests/test_operations.py::TestScientificOperations -v

# Test only finance
pytest tests/test_operations.py::TestFinanceOperations -v

# Test only programming
pytest tests/test_operations.py::TestProgrammingOperations -v
```

## UI Controls

### Basic Mode
- Number buttons (0-9)
- Operators (+, -, *, /, %)
- Decimal point
- Equals (=)
- Clear (C), Clear Entry (CE)
- Backspace (⌫)
- Sign toggle (+/-)
- Memory buttons (MC, MR, M+, M-)

### Scientific Mode
- Angle mode toggle (Degrees/Radians)
- Scientific functions accessible via function buttons
- Full arithmetic operations

### Finance Mode
- Dropdown to select calculation type
- Input fields for parameters
- Calculate button
- Result display

### Programming Mode
- Base selector (BIN, OCT, DEC, HEX)
- Conversion buttons
- Bitwise operation inputs and buttons

## License

MIT License
