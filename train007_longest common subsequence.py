"""
Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

Subsequence
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

Example subsequence
Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".

LCS examples
lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"
Notes
Both arguments will be strings
Return value must be a string
Return an empty string if there exists no common subsequence
Both arguments will have one or more characters (in JavaScript)
All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ),
which would have two possible longest common subsequences: "12" and "34".
Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest
common subsequence will be valid).

Tips
Wikipedia has an explanation of the two properties that can be used to solve the problem:

First property
Second property
"""


#def lcs(x, y):
#    def subseq(sequence):
#        subsequence_list = []
#        for i in range(len(sequence)):
#            temp_str = ""
#            temp_str += sequence[i]
#            subsequence_list.append(sequence[i])
#            for j in range(i+1, len(sequence)):
#                temp_str += sequence[j]
#                subsequence_list.append(temp_str)
#        return subsequence_list
#
#    x_subseq = subseq(x)
#    y_subseq = subseq(y)
#    common_subseq_list = []
#    max_common_subseq = ""
#    for sub_i in x_subseq:
#        if sub_i in y_subseq:
#            if len(sub_i)>len(max_common_subseq):
#                max_common_subseq = sub_i
#    return max_common_subseq

def lcs(x, y):
    max_com_sseq = ""
    flag_1 = 0
    for i in range(len(x)):
        for j in range(flag_1, len(y)):
            if x[i] == y[j]:
                flag_1 = j
                max_com_sseq += x[i]
    pass

