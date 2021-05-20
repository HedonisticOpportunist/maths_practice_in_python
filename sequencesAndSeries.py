def find_nth_term_for_an_arithmetic_sequence(first_term: int, common_difference: int, requested_term: int) -> int:
    """
    Find the nth term in an arithmetic sequence
    :param first_term:
    :param common_difference:
    :param requested_term
    :return: the nth term
    """
    return first_term + (requested_term - 1) * common_difference


def find_the_nth_term_for_a_geometric_sequence(first_term: int, common_ratio: int, requested_term: int) -> int:
    """
    Find the nth term in a geometric sequence
    :param first_term:
    :param common_ratio:
    :param requested_term:
    :return: the nth term
    """
    return first_term * common_ratio ** (requested_term - 1)


def find_sum_of_arithmetic_sequence(requested_terms: int, first_term: int, common_difference: int) -> int:
    """
    Finds the sum of an arithmetic sequence
    :param requested_terms:
    :param first_term:
    :param common_difference:
    :return: the sum of an arithmetic sequence
    """
    return int((requested_terms / 2) * (2 * first_term + (requested_terms - 1) * common_difference))
