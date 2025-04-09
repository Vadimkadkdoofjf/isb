from spicy import special

def long_one_test(seq: str)-> float:
    """
    The function checks sequence using test for the longest sequence in block
    :param seq: our sequence
    :return: result
    """
    n = len(seq)
    m = 8

    if n == 0:
        raise ValueError("Sequence must not be empty")

    pi = [0.2148, 0.3672, 0.2305, 0.1875]

    v = [0, 0, 0, 0]

    for i in range(0, len(seq), m):
        block = seq[i:i + m]
        max_len = current = 0

        for bit in block:
            current = current + 1 if bit == '1' else 0
            max_len = max(max_len, current)

        match max_len:
            case max_len if max_len <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case max_len if max_len >= 4:
                v[3] += 1

    xi_square = sum(((v[i] - 16 * pi[i]) ** 2) / (16 * pi[i]) for i in range(len(v)))
    p_value = special.gammainc((3 / 2), (xi_square / 2))

    return p_value