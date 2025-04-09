import math

def freq_bit_test(seq: str)-> float:
    """
    The function checks sequence using frequency bit test
    :param seq: our sequence
    :return: result
    """
    n = len(seq)

    if n==0:
        raise ValueError("Sequence must not be empty")

    one_count = seq.count("1")
    null_count = seq.count("0")

    s_n = (one_count - null_count)/math.sqrt(n)

    p_value = math.erfc(abs(s_n)/math.sqrt(2))

    return p_value


