"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).

In C++ return in such a case {0, 0}. In F# return [||]. In Kotlin return []

#Examples: gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin return[]`

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.
"""

"""什么是prime number
质数（prime number）又称素数，有无限个。一个大于1的自然数，除了1和它本身外，不能被其他自然数整除，换句话说就是该数除了1和它本身以外不再有其他的因数；否则称为合数。

根据算术基本定理，每一个比1大的整数，要么本身是一个质数，要么可以写成一系列质数的乘积；而且如果不考虑这些质数在乘积中的顺序，那么写出来的形式是唯一的。最小的质数是2。
"""
PRIME = 2


def prime_num():
    global PRIME
    while True:
        yield PRIME
        while True:
            flag = 1
            PRIME += 1
            for i in range(2, PRIME):
                if PRIME % i == 0:
                    flag = 0
            if flag == 1:
                break


def gap(g, m, n):
    prime_list = []
    for i in prime_num():
        if m <= i <= n:
            prime_list.append(i)
        elif i > n:
            break
    for j in range(1, len(prime_list)):
        first_num, second_num = prime_list[j-1], prime_list[j]
        if second_num - first_num == g:
            return [first_num, second_num]
    return None


if __name__ == "__main__":
    print(gap(10, 300, 400))
