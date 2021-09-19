def fib(n):

    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def test_result(k):

    print(f'The number {k} of Fibonacci is {fib(k)}')


m = int(input('Please input your number'))

test_result(m)
