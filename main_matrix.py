from playLA.Matrix import Matrix

if __name__ == '__main__':

    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5,  6], [7, 8]])
    # print(matrix)
    #
    # print("matrix.shape = {}".format(matrix.shape()))
    # print("matrix.size = {}".format(matrix.size()))
    # print("matrix.len = {}".format(len(matrix)))
    # print("matrix = {}".format(matrix[0, 0]))
    # print("matrix[{}] = {}".format(0, matrix.row_vector(0)))
    # print("matrix[{}] = {}".format(0, matrix.col_vector(0)))

    print("{} + {} = {}".format(matrix, matrix2, matrix + matrix2))
    print("{} - {} = {}".format(matrix, matrix2, matrix - matrix2))
    print("{} * {} = {}".format(2, matrix, 2 * matrix))
    print("{} * {} = {}".format(matrix, 2, matrix * 2))

    print("zero = {}".format(Matrix.zero(2, 3)))
