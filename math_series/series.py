def fibonacci(n):
    """
    Fibonacci through iteration
    """
    seq_list = [0, 1]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]


def lucas(n):
    """
    Lucas testing - iteration
    """

    seq_list = [2, 1]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]


def sum_series(n, first=0, second=1):
    """
    Sum Series testing
    """

    seq_list = [first, second]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]
