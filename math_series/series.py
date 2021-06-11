def fibonacci(n):
    """
    Fibonacci testing with one parameter n, returning the nth value int he fibonacci series. Implemented through iteration.
    """
    seq_list = [0, 1]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]


def lucas(n):
    """
    Lucas testing that returns the nth value in lucas numbers through iteration
    """

    seq_list = [2, 1]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]


def sum_series(n, first=0, second=1):
    """
    Sum Series testing with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional paraments will have default values of 0 and 1, and will determine the first two values for the series to be produced.
    """

    seq_list = [first, second]
    for i in range(2, n + 1):
        next_n = seq_list[-1] + seq_list[-2]
        seq_list.append(next_n)
    return seq_list[n - 1]
