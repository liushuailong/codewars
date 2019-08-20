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
    #return None