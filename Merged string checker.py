"""At a job interview, you are challenged to write an algorithm
to check if a given string, s, can be formed from two other
strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""

def is_merge(s, part1, part2):
    s_list = []
    sum_par = part1 + part2
    sum_list = []
    for i in s:
        s_list.append(i)
    s_list.sort()
    for j in sum_par:
        sum_list.append(j)
    sum_list.sort()
    if len(s_list) != len(sum_list):
        return False
    else:
        for y in range(len(s_list)):
            if s_list[y] != sum_list[y]:
                return False
            else:
                flag_1 = 0
                for i in part1:
                    for j in range(flag_1, len(s)):
                        flag_1_1 = 0
                        if i == s[j]:
                            flag_1 = j
                            flag_1_1 = 1
                            break
                    if flag_1_1 == 0:
                        return False

                flag_2 = 0
                for i_1 in part2:
                    for j_1 in range(flag_2, len(s)):
                        flag_2_2 = 0
                        if i_1 == s[j_1]:
                            flag_2 = j_1
                            flag_2_2 = 1
                            break
                    if flag_2_2 == 0:
                        return False
    return True


if __name__ == "__main__":
    s = "codewars"
    part1 = "cwdr"
    part2 = "oeas"
    if is_merge(s, part1, part2):
        print("ok")
    else:
        print("no")
