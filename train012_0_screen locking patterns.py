"""
Screen Locking Patterns
You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure. To
unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger without lifting it as
you trace the pattern through the screen. The image below has an example pattern of 7 dots/points: [A, B, I, E, D, G, C].

lock_example.png

For this kata, your job is to implement the function countPatternsFrom(firstPoint, length); where firstPoint is a single
-character string corresponding to the point in the grid (i.e.: 'A') and length is an integer indicating the length of
the pattern. The function must return the number of combinations starting from the given point, that have the given
length.

Take into account that dots can only be connected with straight directed lines either:

horizontally (like A to B)
vertically (like D to G),
diagonally (like I and E, as well as B and I), or
passing over a point that has already been 'used' like (G and C passing over E).
The sample tests have some examples of the number of combinations for some cases to help you check your code.

Optional Extra:

Out of curiosity, in case you're wondering, for the Android lock screen, valid patterns must have between 4 and 9 dots,
and there are 389112 possible valid combinations in total.

Haskell Note: A data type Vertex is provided in place of the single-character strings. See the solution setup code for
more details.
"""


def count_patterns_from(firstPoint, length):
    # Your code here!
    pass
