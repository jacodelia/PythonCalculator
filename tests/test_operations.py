import pytest
import math
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations import ArithmeticOperations, ScientificOperations, FinanceOperations, ProgrammingOperations


class TestArithmeticOperations:
    def setup_method(self):
        self.arith = ArithmeticOperations()

    def test_add(self):
        assert self.arith.add(2, 3) == 5
        assert self.arith.add(-1, 1) == 0
        assert self.arith.add(0, 0) == 0
        assert self.arith.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        assert self.arith.subtract(5, 3) == 2
        assert self.arith.subtract(3, 5) == -2
        assert self.arith.subtract(0, 0) == 0

    def test_multiply(self):
        assert self.arith.multiply(2, 3) == 6
        assert self.arith.multiply(-2, 3) == -6
        assert self.arith.multiply(0, 5) == 0
        assert self.arith.multiply(2.5, 2) == 5.0

    def test_divide(self):
        assert self.arith.divide(6, 2) == 3
        assert self.arith.divide(5, 2) == 2.5
        assert self.arith.divide(10, -2) == -5
        assert self.arith.divide(5, 0) is None

    def test_modulo(self):
        assert self.arith.modulo(10, 3) == 1
        assert self.arith.modulo(10, 2) == 0
        assert self.arith.modulo(5, 0) is None

    def test_power(self):
        assert self.arith.power(2, 3) == 8
        assert self.arith.power(4, 0.5) == 2
        assert self.arith.power(2, -1) == 0.5

    def test_square_root(self):
        assert self.arith.square_root(4) == 2
        assert self.arith.square_root(2) == pytest.approx(1.41421356, rel=1e-6)
        assert self.arith.square_root(-1) is None

    def test_percentage(self):
        assert self.arith.percentage(100, 10) == 10
        assert self.arith.percentage(50, 25) == 12.5

    def test_negate(self):
        assert self.arith.negate(5) == -5
        assert self.arith.negate(-5) == 5

    def test_reciprocal(self):
        assert self.arith.reciprocal(2) == 0.5
        assert self.arith.reciprocal(0.5) == 2
        assert self.arith.reciprocal(0) is None

    def test_factorial(self):
        assert self.arith.factorial(0) == 1
        assert self.arith.factorial(1) == 1
        assert self.arith.factorial(5) == 120
        assert self.arith.factorial(10) == 3628800
        assert self.arith.factorial(-1) is None

    def test_absolute(self):
        assert self.arith.absolute(5) == 5
        assert self.arith.absolute(-5) == 5
        assert self.arith.absolute(0) == 0


class TestScientificOperations:
    def setup_method(self):
        self.sci = ScientificOperations()

    def test_sin_degrees(self):
        assert self.sci.sin(0, degrees=True) == 0
        assert self.sci.sin(90, degrees=True) == pytest.approx(1, rel=1e-6)
        assert self.sci.sin(30, degrees=True) == pytest.approx(0.5, rel=1e-6)

    def test_sin_radians(self):
        assert self.sci.sin(0, degrees=False) == 0
        assert self.sci.sin(math.pi/2, degrees=False) == pytest.approx(1, rel=1e-6)

    def test_cos_degrees(self):
        assert self.sci.cos(0, degrees=True) == 1
        assert self.sci.cos(90, degrees=True) == pytest.approx(0, rel=1e-6)
        assert self.sci.cos(60, degrees=True) == pytest.approx(0.5, rel=1e-6)

    def test_tan_degrees(self):
        assert self.sci.tan(0, degrees=True) == 0
        assert self.sci.tan(45, degrees=True) == pytest.approx(1, rel=1e-6)

    def test_asin(self):
        assert self.sci.asin(0, degrees=True) == 0
        assert self.sci.asin(1, degrees=True) == pytest.approx(90, rel=1e-6)
        assert self.sci.asin(2, degrees=True) is None

    def test_acos(self):
        assert self.sci.acos(1, degrees=True) == 0
        assert self.sci.acos(0, degrees=True) == pytest.approx(90, rel=1e-6)
        assert self.sci.acos(2, degrees=True) is None

    def test_atan(self):
        assert self.sci.atan(0, degrees=True) == 0
        assert self.sci.atan(1, degrees=True) == pytest.approx(45, rel=1e-6)

    def test_sinh(self):
        assert self.sci.sinh(0) == 0
        assert self.sci.sinh(1) == pytest.approx(1.17520119, rel=1e-6)

    def test_cosh(self):
        assert self.sci.cosh(0) == 1
        assert self.sci.cosh(1) == pytest.approx(1.54308063, rel=1e-6)

    def test_tanh(self):
        assert self.sci.tanh(0) == 0
        assert self.sci.tanh(100) == pytest.approx(1, rel=1e-6)

    def test_log(self):
        assert self.sci.log(100) == 2
        assert self.sci.log(10, 10) == 1
        assert self.sci.log(10, math.e) == pytest.approx(2.302585, rel=1e-3)
        assert self.sci.log(0) is None

    def test_ln(self):
        assert self.sci.ln(1) == 0
        assert self.sci.ln(math.e) == 1
        assert self.sci.ln(0) is None

    def test_exp(self):
        assert self.sci.exp(0) == 1
        assert self.sci.exp(1) == pytest.approx(math.e, rel=1e-6)

    def test_power(self):
        assert self.sci.power(2, 3) == 8
        assert self.sci.power(4, 0.5) == 2

    def test_nth_root(self):
        assert self.sci.nth_root(8, 3) == 2
        assert self.sci.nth_root(16, 4) == 2
        assert self.sci.nth_root(-8, 3) == -2

    def test_cube_root(self):
        assert self.sci.cube_root(8) == 2
        assert self.sci.cube_root(-8) == -2

    def test_factorial(self):
        assert self.sci.factorial(5) == 120
        assert self.sci.factorial(0) == 1
        assert self.sci.factorial(-1) is None

    def test_combinations(self):
        assert self.sci.combinations(5, 2) == 10
        assert self.sci.combinations(10, 0) == 1
        assert self.sci.combinations(5, 6) is None

    def test_permutations(self):
        assert self.sci.permutations(5, 2) == 20
        assert self.sci.permutations(5, 0) == 1
        assert self.sci.permutations(5, 6) is None

    def test_gamma(self):
        assert self.sci.gamma(5) == 24
        assert self.sci.gamma(0.5) == pytest.approx(math.sqrt(math.pi), rel=1e-3)

    def test_ceil(self):
        assert self.sci.ceil(2.3) == 3
        assert self.sci.ceil(5) == 5

    def test_floor(self):
        assert self.sci.floor(2.7) == 2
        assert self.sci.floor(5) == 5

    def test_random(self):
        result = self.sci.random()
        assert 0 <= result < 1

    def test_randint(self):
        for _ in range(100):
            result = self.sci.randint(1, 10)
            assert 1 <= result <= 10

    def test_prime_factorization(self):
        assert self.sci.prime_factorization(12) == [2, 2, 3]
        assert self.sci.prime_factorization(7) == [7]
        assert self.sci.prime_factorization(1) == []

    def test_is_prime(self):
        assert self.sci.is_prime(2) is True
        assert self.sci.is_prime(3) is True
        assert self.sci.is_prime(4) is False
        assert self.sci.is_prime(1) is False

    def test_gcd(self):
        assert self.sci.gcd(12, 8) == 4
        assert self.sci.gcd(7, 13) == 1

    def test_lcm(self):
        assert self.sci.lcm(4, 6) == 12

    def test_complex_operations(self):
        a = complex(1, 2)
        b = complex(3, 4)
        assert self.sci.complex_add(a, b) == complex(4, 6)
        assert self.sci.complex_subtract(a, b) == complex(-2, -2)
        assert self.sci.complex_multiply(a, b) == complex(-5, 10)
        assert self.sci.complex_divide(a, b) == pytest.approx(complex(0.44, 0.08), rel=1e-1)
        assert self.sci.complex_magnitude(complex(3, 4)) == 5

    def test_to_scientific_notation(self):
        result = self.sci.to_scientific_notation(1234.56)
        assert 'e' in result.lower()


class TestFinanceOperations:
    def setup_method(self):
        self.finance = FinanceOperations()

    def test_simple_interest(self):
        result = self.finance.simple_interest(1000, 5, 2)
        assert result == 1100

    def test_compound_interest(self):
        result = self.finance.compound_interest(1000, 10, 1, 1)
        assert result == 1100
        result = self.finance.compound_interest(1000, 10, 1, 2)
        assert result == pytest.approx(1102.5, rel=1e-1)

    def test_present_value(self):
        result = self.finance.present_value(1100, 10, 1)
        assert result == pytest.approx(1000, rel=1e-1)

    def test_future_value(self):
        result = self.finance.future_value(1000, 10, 1)
        assert result == pytest.approx(1100, rel=1e-1)

    def test_payment(self):
        result = self.finance.payment(100000, 5, 360)
        assert result == pytest.approx(536.82, rel=1e-1)

    def test_roi(self):
        assert self.finance.roi(1000, 1500) == 50

    def test_cagr(self):
        result = self.finance.cagr(100, 200, 2)
        assert result == pytest.approx(41.42, rel=1e-1)

    def test_depreciation_straight_line(self):
        result = self.finance.depreciation_straight_line(10000, 1000, 5)
        assert result == 1800

    def test_depreciation_double_declining_balance(self):
        result = self.finance.depreciation_double_declining_balance(10000, 5, 1)
        assert result == 4000

    def test_tip_calculator(self):
        result = self.finance.tip_calculator(100, 20, 2)
        assert result == 60

    def test_tax_calculator(self):
        result = self.finance.tax_calculator(100, 10)
        assert result == pytest.approx(110, rel=1e-6)

    def test_discount(self):
        result = self.finance.discount(100, 20)
        assert result == 80


class TestProgrammingOperations:
    def setup_method(self):
        self.prog = ProgrammingOperations()

    def test_from_decimal_to_binary(self):
        assert self.prog.from_decimal(10, 2) == "1010"
        assert self.prog.from_decimal(0, 2) == "0"
        assert self.prog.from_decimal(255, 2) == "11111111"

    def test_from_decimal_to_octal(self):
        assert self.prog.from_decimal(10, 8) == "12"
        assert self.prog.from_decimal(64, 8) == "100"

    def test_from_decimal_to_hex(self):
        assert self.prog.from_decimal(255, 16) == "FF"
        assert self.prog.from_decimal(16, 16) == "10"

    def test_to_decimal_from_binary(self):
        assert self.prog.to_decimal("1010", 2) == 10
        assert self.prog.to_decimal("FF", 16) == 255
        assert self.prog.to_decimal("12", 8) == 10

    def test_to_binary(self):
        assert self.prog.to_binary("10") == "1010"
        assert self.prog.to_binary("255") == "11111111"

    def test_to_octal(self):
        assert self.prog.to_octal("10") == "12"

    def test_to_hexadecimal(self):
        assert self.prog.to_hexadecimal("255") == "FF"

    def test_bitwise_and(self):
        assert self.prog.bitwise_and(12, 10) == 8

    def test_bitwise_or(self):
        assert self.prog.bitwise_or(12, 10) == 14

    def test_bitwise_xor(self):
        assert self.prog.bitwise_xor(12, 10) == 6

    def test_bitwise_not(self):
        assert self.prog.bitwise_not(5) == -6

    def test_left_shift(self):
        assert self.prog.left_shift(1, 3) == 8

    def test_right_shift(self):
        assert self.prog.right_shift(8, 2) == 2

    def test_bit_count(self):
        assert self.prog.bit_count(7) == 3
        assert self.prog.bit_count(8) == 1

    def test_bit_length(self):
        assert self.prog.bit_length(5) == 3
        assert self.prog.bit_length(8) == 4

    def test_rotate_left(self):
        assert self.prog.rotate_left(0b00011100, 2, 8) == 0b01110000

    def test_rotate_right(self):
        assert self.prog.rotate_right(0b00011100, 2, 8) == 0b00000111

    def test_get_bit(self):
        assert self.prog.get_bit(8, 3) == 1
        assert self.prog.get_bit(8, 0) == 0

    def test_set_bit(self):
        assert self.prog.set_bit(0, 3) == 8

    def test_clear_bit(self):
        assert self.prog.clear_bit(15, 2) == 11

    def test_toggle_bit(self):
        assert self.prog.toggle_bit(10, 1) == 8

    def test_ones_complement(self):
        assert self.prog.ones_complement(5) == 0xFFFFFFFA

    def test_twos_complement(self):
        assert self.prog.twos_complement(1, 8) == 255

    def test_is_power_of_two(self):
        assert self.prog.is_power_of_two(8) is True
        assert self.prog.is_power_of_two(7) is False
        assert self.prog.is_power_of_two(0) is False

    def test_next_power_of_two(self):
        assert self.prog.next_power_of_two(5) == 8
        assert self.prog.next_power_of_two(8) == 8
        assert self.prog.next_power_of_two(1) == 1

    def test_hex_to_rgb(self):
        assert self.prog.hex_to_rgb("#FF0000") == (255, 0, 0)
        assert self.prog.hex_to_rgb("#00FF00") == (0, 255, 0)

    def test_rgb_to_hex(self):
        assert self.prog.rgb_to_hex(255, 0, 0) == "#FF0000"
        assert self.prog.rgb_to_hex(0, 255, 0) == "#00FF00"

    def test_ascii_to_char(self):
        assert self.prog.ascii_to_char(65) == "A"
        assert self.prog.ascii_to_char(97) == "a"

    def test_char_to_ascii(self):
        assert self.prog.char_to_ascii("A") == 65
        assert self.prog.char_to_ascii("a") == 97


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
