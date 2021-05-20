import numberSystems

# binary to decimal
print(numberSystems.convert_into_decimal("101010", 2))

# octal number to decimal
print(numberSystems.convert_into_decimal("325", 8))

# decimal to binary conversion
print(numberSystems.create_number_system_list(83, 2))

# decimal to octal conversion
print(numberSystems.create_number_system_list(1001, 8))

# hexadecimal to decimal
print(numberSystems.convert_hex_into_decimal("F9B3"))

# decimal to hexadecimal
print(numberSystems.convert_decimal_to_hexadecimal(14397))
