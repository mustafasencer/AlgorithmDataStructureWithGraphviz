fib_results = {}


def fib(n):
    if n in fib_results:
        return fib_results[n]
    if n < -1:
        val = (-1) ^ (abs(n) + 1) * fib(abs(n))
    elif n == -1:
        val = 1
    elif n == 0 or n == 1:
        val = n
    else:
        val = fib(n - 1) + fib(n - 2)

    fib_results[n] = val
    return val


def fibonacci(n):
    a = 0
    b = 1
    if n < -1:
        for i in range(-2, n - 1, -1):
            c = a + b
            a = b
            b = c
        return b
    elif n == -1:
        return 1
    elif n == 0 or n == 1:
        return n
    else:
        for i in range(n):
            c = a + b
            a = b
            b = c
        return b


def fibonacci_positive(n):
    a = 0
    b = 1
    if n == 0 or n == 1:
        return n
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return b


if __name__ == '__main__':
    fibonacci_positive(6)
    fibonacci(10)
