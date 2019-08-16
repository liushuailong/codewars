"""
You have to create a function that takes a positive integer number and
returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""


def next_bigger(n):
    digits_list = []
    if 0 <= n < 10:
        return -1
    temp_n = n
    while temp_n:
        digits_list.append(temp_n % 10)
        temp_n = temp_n // 10

    flag_2 = 0
    for i in range(1, len(digits_list)):
        if digits_list[i - 1] > digits_list[i]:
            flag_2 = i
            break
    if flag_2 == 0:
        return -1
    next_big_list = (list(sorted(digits_list[:flag_2], reverse=True)) + digits_list[flag_2:])
    for j in range(flag_2+1):
        if next_big_list[flag_2] < next_big_list[flag_2-j]:
            next_big_list[flag_2], next_big_list[flag_2-j] = next_big_list[flag_2-j], next_big_list[flag_2]
            break
    next_big = 0
    for i in range(len(digits_list)):
        next_big += next_big_list[i] * (10 ** i)
    return next_big


if __name__ == "__main__":
    text_num = 27753152368
    print(next_bigger(27753138652))
    if text_num == next_bigger(27753138652):
        print("ok")
    else:
        print("no")
