def common_divisor_2integers(num_1, num_2):
    """
    :param num_1: interger
    :param num_2: interger
    :return: max common divisor
    """
    """ 求两个数的最大公约数(method):  辗转相除法：辗转相除法是求两个自然数的最大公约数的一种方法，也叫欧几里德算法。"""
    max_num = 0
    min_num = 0
    if num_1 < num_2:
        max_num = num_2
        min_num = num_1
    else:
        max_num = num_1
        min_num = num_2
    r = max_num % min_num
    if r == 0:
        return min_num
    while r != 0:
        r = max_num % min_num
        max_num, min_num = min_num, r
    return max_num


def common_maulitples_2integers(num_1, num_2):
    """" 求两个数的最小公倍数"""
    max_common_divisor_2integers = common_divisor_2integers(num_1, num_2)
    return int(num_1 * num_2 / max_common_divisor_2integers)


def convertFracts(lst):
    new_lst = []
    first_num = 0
    if not lst:
        return lst
    for i in range(len(lst)):
        if 0 == i:
            first_num = lst[i][1]
        else:
            second_num = lst[i][1]
            max_num = common_maulitples_2integers(first_num, second_num)
            first_num = max_num
    max_com_mau = first_num

    for j in lst:
        new_lst.append([int(j[0] * max_com_mau / j[1]), max_com_mau])
    return new_lst


if __name__ == "__main__":
    a = [[1, 200], [3, 1000], [1, 2500], [1, 20000]]
    c = convertFracts(a)
    print(c)
    b = common_divisor_2integers(5000, 20000)
    print(b)

