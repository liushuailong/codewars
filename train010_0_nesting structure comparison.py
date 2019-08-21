"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the
same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

"""

def same_structure_as(original,other):
    for x, y in zip(original, other):
        if type(x) != type(y):
            return False
        else:
            if type(x) == type(list):
                same_structure_as(x, y)
            else:
                return True

if __name__ == "__main__":
    if same_structure_as([1,[1,1]],[[2,2],2]):
        print("ok")
    else:
        print("no")

