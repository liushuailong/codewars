"""
Write an algorithm that takes an array and moves all of the zeros
 to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    zeros_list = []
    nonzeros_list = []
    for i in array:
        if i == 0:
            if (type(i) == int) | (type(i) == float):
                zeros_list.append(i)
            else:
                nonzeros_list.append(i)
        else:
            nonzeros_list.append(i)
    return nonzeros_list + zeros_list


if __name__ == "__main__":
    text = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    new_text = [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    if new_text == move_zeros(text):
        print("ok")
    else:
        print('No')