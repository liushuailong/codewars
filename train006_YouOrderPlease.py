"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position
the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive
numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""
import re


def order(sentence):
    """
    order the words unordered in the string and return the correct sentence.
    :param sentence: the unordered sentence
    :return: the correct sentence
    """
    sent_list = sentence.split(" ")
    temp_list = []
    new_sent = ""
    if not len(sentence):
        return sentence
    for sent in sent_list:
        match_num = re.match(r".*(\d).*", sent)
        temp_list.append((match_num.group(1), sent))
    temp_list.sort()
    for i in range(len(temp_list)):
        if i == 0:
            new_sent += temp_list[i][1]
        else:
            new_sent += " " + temp_list[i][1]
    return new_sent


# 利用了正则表达式提取字符串中的数字，并返回；
# 利用的列表的排序去对字符串进行排序；