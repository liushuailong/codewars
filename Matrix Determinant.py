def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        matrix_len = len(matrix)
        first_line_len = len(matrix[0])
        result = 0
        for i in range(first_line_len):
            matrix_minor = matrix
            del matrix_minor[0]
            for j in matrix_minor:
                del j[i]
            result += i*determinant(matrix_minor)
        return result


if __name__ == "__main__":
    m1 = [[1, 3], [2, 5]]
    m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
    print(determinant([[1]]))
    print(determinant(m1))
    determinant(m2)