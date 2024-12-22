"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty array A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of array A, B is an integer within the range [1..2,147,483,647].

"""


def solution(A, B):
    min_prime = 2
    result = 0

    for i, j in zip(A, B):
        i_primes = set()
        j_primes = set()

        while min_prime <= i:
            if i % min_prime == 0:
                i_primes.add(min_prime)
                i /= min_prime
            else:
                min_prime += 1

        min_prime = 2
        while min_prime <= j:
            if j % min_prime == 0:
                j_primes.add(min_prime)
                j /= min_prime
            else:
                min_prime += 1

        if i_primes and j_primes and i_primes == j_primes:
            result += 1
    return 1


def solution_(A, B):
    z = len(A)
    result = 0
    for index in range(z):
        a = A[index]
        b = B[index]
        d = gcd(a, b)
        if has_diff_factor(d, a):
            continue
        if has_diff_factor(d, b):
            continue
        result += 1

    return result


def has_diff_factor(a, b):
    div = gcd(a, b)
    while div != 1:
        b /= div
        div = gcd(a, b)
    return a % b != 0


def gcd(a, b):
    while a >= 0 and b >= 0:
        a_mod_b = a % b
        if a_mod_b == 0:
            return b
        a = b
        b = a_mod_b

    return 1


if __name__ == "__main__":
    A = [15, 10, 3]
    B = [75, 30, 5]
    result = solution_(A, B)
    assert result == 1
    print(result)
