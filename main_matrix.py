from playLA.Matrix import Matrix

if __name__ == '__main__':

    matrix = Matrix([[1, 211], [31, 4]])
    print(matrix)

    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("matrix.len = {}".format(len(matrix)))
    print("matrix = {}".format(matrix[0, 0]))
    print("matrix[{}] = {}".format(0, matrix.row_vector(0)))
    print("matrix[{}] = {}".format(0, matrix.col_vector(0)))

