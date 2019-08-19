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
    digits_list[flag_2 - 1], digits_list[flag_2] = digits_list[flag_2], digits_list[flag_2 - 1]
    next_big_list = (sorted(digits_list[:flag_2], reverse=True) + digits_list[flag_2:])
    next_big = 0
    for i in range(len(digits_list)):
        next_big += digits_list[i] * (10 ** i)

    return next_big

