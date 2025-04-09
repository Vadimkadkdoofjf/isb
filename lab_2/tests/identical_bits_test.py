import math


def ident_test(seq: str)-> float:
    """
    The function checks sequence using identical bit test
    :param seq: our sequence
    :return: result
    """

    n = len(seq)

    if n == 0:
        raise ValueError("Sequence must not be empty")

    zeta = seq.count("1")/n

    if abs(zeta - 0.5) >= 2 / math.sqrt(n):
        return 0

    v_n = 0

    for i in range(n - 1):
        if seq[i] != seq[i + 1]:
            v_n += 1

    p_value = math.erfc(abs(v_n - 2 * n * zeta * (1 - zeta))/
                        (2 * math.sqrt(2 * n) * zeta * (1 - zeta)))

    return p_value