"""
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C,
C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is
a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing
whitespace: you can use dynamically allocated character strings.

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


def sum_for_list(lst):
    # search the max num in list
    max_num = max(lst)
    # create a new list named result_list to store the result
    result_list = []
    for prime_number in prime_num():
        sum_prime = 0
        flag = 0
        if prime_number > max_num:
            break
        for num in lst:
            if num % prime_number == 0:
                sum_prime += num
                flag = 1
        if sum_prime:
            result_list.append([prime_number, sum_prime])
        elif sum_prime == 0 and flag == 1:
            result_list.append([prime_number, sum_prime])
    return result_list


if __name__ == "__main__":
    a = sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100])
    print(a)