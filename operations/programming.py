import math
from typing import Optional


class ProgrammingOperations:
    def __init__(self):
        self.current_base = 10

    def set_base(self, base: int):
        if base in (2, 8, 10, 16):
            self.current_base = base

    def get_base(self) -> int:
        return self.current_base

    @staticmethod
    def from_decimal(value: int, target_base: int) -> str:
        if target_base not in (2, 8, 10, 16):
            return str(value)
        
        if value == 0:
            return "0"
        
        negative = value < 0
        value = abs(value)
        
        digits = "0123456789ABCDEF"
        result = ""
        
        while value > 0:
            result = digits[value % target_base] + result
            value //= target_base
        
        return "-" + result if negative else result

    @staticmethod
    def to_decimal(value: str, source_base: int) -> Optional[int]:
        if source_base not in (2, 8, 10, 16):
            return None
        
        try:
            if source_base == 16:
                return int(value, 16)
            elif source_base == 2:
                return int(value, 2)
            elif source_base == 8:
                return int(value, 8)
            else:
                return int(value)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def to_binary(value: str, source_base: int = 10) -> Optional[str]:
        decimal_val = ProgrammingOperations.to_decimal(value, source_base)
        if decimal_val is None:
            return None
        return ProgrammingOperations.from_decimal(decimal_val, 2)

    @staticmethod
    def to_octal(value: str, source_base: int = 10) -> Optional[str]:
        decimal_val = ProgrammingOperations.to_decimal(value, source_base)
        if decimal_val is None:
            return None
        return ProgrammingOperations.from_decimal(decimal_val, 8)

    @staticmethod
    def to_hexadecimal(value: str, source_base: int = 10) -> Optional[str]:
        decimal_val = ProgrammingOperations.to_decimal(value, source_base)
        if decimal_val is None:
            return None
        return ProgrammingOperations.from_decimal(decimal_val, 16)

    @staticmethod
    def bitwise_and(a: int, b: int) -> int:
        return a & b

    @staticmethod
    def bitwise_or(a: int, b: int) -> int:
        return a | b

    @staticmethod
    def bitwise_xor(a: int, b: int) -> int:
        return a ^ b

    @staticmethod
    def bitwise_not(a: int) -> int:
        return ~a

    @staticmethod
    def left_shift(a: int, bits: int) -> int:
        return a << bits

    @staticmethod
    def right_shift(a: int, bits: int) -> int:
        return a >> bits

    @staticmethod
    def bit_count(a: int) -> int:
        return bin(a).count('1')

    @staticmethod
    def bit_length(a: int) -> int:
        return a.bit_length()

    @staticmethod
    def rotate_left(a: int, bits: int, width: int = 8) -> int:
        a = a & ((1 << width) - 1)
        return ((a << bits) | (a >> (width - bits))) & ((1 << width) - 1)

    @staticmethod
    def rotate_right(a: int, bits: int, width: int = 8) -> int:
        a = a & ((1 << width) - 1)
        return ((a >> bits) | (a << (width - bits))) & ((1 << width) - 1)

    @staticmethod
    def get_bit(a: int, pos: int) -> int:
        return (a >> pos) & 1

    @staticmethod
    def set_bit(a: int, pos: int) -> int:
        return a | (1 << pos)

    @staticmethod
    def clear_bit(a: int, pos: int) -> int:
        return a & ~(1 << pos)

    @staticmethod
    def toggle_bit(a: int, pos: int) -> int:
        return a ^ (1 << pos)

    @staticmethod
    def ones_complement(a: int) -> int:
        return ~a & 0xFFFFFFFF

    @staticmethod
    def twos_complement(a: int, bits: int = 8) -> int:
        return ((~a) + 1) & ((1 << bits) - 1)

    @staticmethod
    def sign_extend(value: int, from_bits: int, to_bits: int) -> int:
        sign_bit = 1 << (from_bits - 1)
        if value & sign_bit:
            value |= (~0 << from_bits)
        value &= (1 << to_bits) - 1
        return value

    @staticmethod
    def to_unsigned(a: int, bits: int) -> int:
        return a & ((1 << bits) - 1)

    @staticmethod
    def to_signed(a: int, bits: int) -> int:
        sign_bit = 1 << (bits - 1)
        if a & sign_bit:
            return a - (1 << bits)
        return a

    @staticmethod
    def min_value(bits: int) -> int:
        return -(1 << (bits - 1))

    @staticmethod
    def max_value(bits: int) -> int:
        return (1 << (bits - 1)) - 1

    @staticmethod
    def is_power_of_two(a: int) -> bool:
        return a > 0 and (a & (a - 1)) == 0

    @staticmethod
    def next_power_of_two(a: int) -> int:
        if a <= 1:
            return 1
        return 1 << (a - 1).bit_length()

    @staticmethod
    def swap_bytes(a: int) -> int:
        return int.from_bytes(a.to_bytes(2, byteorder='big'), byteorder='little')

    @staticmethod
    def hex_to_rgb(hex_color: str) -> Optional[tuple]:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            return None
        try:
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            return None

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> Optional[str]:
        if not all(0 <= x <= 255 for x in (r, g, b)):
            return None
        return f"#{r:02X}{g:02X}{b:02X}"

    @staticmethod
    def ascii_to_char(code: int) -> Optional[str]:
        if 0 <= code <= 127:
            return chr(code)
        return None

    @staticmethod
    def char_to_ascii(char: str) -> Optional[int]:
        if not char:
            return None
        return ord(char[0])
