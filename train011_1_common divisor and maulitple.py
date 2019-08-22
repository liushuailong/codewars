def common_divisor_2integers(a, b):
    max_num = 0
    min_num = 0
    if a==0 or b==0:
        return "pls input integers!"
    if a<b :
        max_num = b
        min_num = a
    else:
        max_num = a
        min_num = b
    r = max_num%min_num
    while r != 0:
        r = max_num%min_num
        max_num = min_num
        min_num = r
    return max_num
def common_maulitples_2integers(a, b):
    if a==0 or b==0:
        return "pls input integers!"
    max_common_divisor_2integers = common_divisor_2integers(a, b)
    return int(a*b/max_common_divisor_2integers)
def main():
    a = common_divisor_2integers(17, 15)
    b = common_maulitples_2integers(17, 15)
    c = common_maulitples_2integers(0, 15)
    print(a, b, c)


if __name__ == '__main__':
    main()
