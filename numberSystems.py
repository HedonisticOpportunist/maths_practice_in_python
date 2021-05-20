def calculate_modulo(number_one: int, number_two: int) -> int:
    """
    Calculate the modulus of two numbers
    :param number_one:
    :param number_two:
    :return: the modulus
    """
    return number_one % number_two


def create_number_system_list(number: int, base: int):
    """
    Create a number list based on the base
    :param number:
    :param base:
    :return: a reversed numbers list
    """
    numbers_list = []
    while number != 0:
        remainder = calculate_modulo(number, base)
        numbers_list.append(remainder)
        number = int(number / base)
    numbers_list.reverse()
    return numbers_list


def convert_into_decimal(non_binary_number: str, base: int) -> int:
    """
   Converts a non binary string number into a decimal number
   :param non_binary_number:
   :param base:
   :return: a decimal number
   """
    decimal_number = 0
    for digit in range(len(non_binary_number)):
        decimal_number += int(non_binary_number[digit]) * base ** abs((digit - (len(non_binary_number) - 1)))
    return decimal_number


def convert_hex_into_decimal(hex_number: str) -> int:
    """
    Converts a hexadecimal number into a decimal
    :param hex_number:
    :return:
    """
    return int(hex_number, 16)


def convert_decimal_to_hexadecimal(decimal: int) -> str:
    """
    Returns a decimal number into a hexadecimal
    :param decimal:
    :return: a hexadecimal string
    """
    return hex(decimal)
