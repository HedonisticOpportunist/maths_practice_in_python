import numberSystems
import sequencesAndSeries

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

# find the nth term in an arithmetic sequence
print(sequencesAndSeries.find_nth_term_for_an_arithmetic_sequence(3, 5, 10))

# find the nth term in a geometric sequence
print(sequencesAndSeries.find_the_nth_term_for_a_geometric_sequence(2, 3, 7))

# find the sum of an arithmetic sequence
print(sequencesAndSeries.find_sum_of_arthimetic_sequence(10, 3, 4))
