"""
Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle.
A Boggle board is a 2D array of individual characters, e.g.:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]
Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally)
without re-using any previously used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses, while "BUNGIE", "BINS",
and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return true or false depending on whether
the string is found in the array as per Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to 150x150 and strings up to 150 uppercase
letters). You do not have to check whether the string is a real word or not, only if it's a valid guess.
"""


def scan_char(board_temp, tuple_char, achar):
    """
    scan the board around about the tuple_char, judge weather equal to the achar.
    :param board_temp:  array
    :param tuple_char: array[tuple_char[0]][tuple_char[1]]
    :param achar: the char in word
    :return: list of tuple if match , else []
    """
    result_set = set()
    for (i, j) in tuple_char:
        if 0 <= (i - 1) and 0 <= (j - 1) and board_temp[i - 1][j - 1] == achar:
            result_set.add((i - 1, j - 1))
        elif 0 <= (i - 1) and board_temp[i - 1][j] == achar:
            result_set.add((i - 1, j))
        elif 0 <= (i - 1) and (j + 1) <= len(board_temp[0]) - 1 and board_temp[i - 1][j + 1] == achar:
            result_set.add((i - 1, j + 1))
        elif 0 <= (j - 1) and board_temp[i][j - 1] == achar:
            result_set.add((i, j - 1))
        elif (j + 1) <= len(board_temp[0]) - 1 and board_temp[i][j + 1] == achar:
            result_set.add((i, j + 1))
        elif 0 <= (j - 1) and (i + 1) <= len(board_temp) - 1 and board_temp[i - 1][j + 1] == achar:
            result_set.add((i + 1, j - 1))
        elif (i + 1) <= len(board_temp) - 1 and board_temp[i + 1][j] == achar:
            result_set.add((i + 1, j))
        elif (i + 1) <= len(board_temp) - 1 and (j + 1) <= len(board_temp[0]) - 1 and board_temp[i + 1][j] == achar:
            result_set.add((i + 1, j + 1))
    return result_set


def find_word(board, word):
    tuple_set = set()
    for num_1 in range(len(word)):
        if num_1 == 0:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if word[num_1] == board[i][j]:
                        tuple_set.add((i, j))
            if not tuple_set:
                return False
        else:
            temp_set = scan_char(board, tuple_set, word[num_1])
            if not temp_set:
                return False
            tuple_set = temp_set - tuple_set
    return True


