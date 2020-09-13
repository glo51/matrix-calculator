def matrix1():
    mat1 = []
    size1 = input('Enter size of first matrix: ').split()
    print('Enter first matrix:')
    for n in range(int(size1[0])):
        row = list(input().split(' '))
        mat1.append(row)
    return size1, mat1


def matrix2():
    mat2 = []
    size2 = input('Enter size of second matrix: ').split()
    print('Enter second matrix:')
    for n in range(int(size2[0])):
        row = list(input().split(' '))
        mat2.append(row)
    return size2, mat2


def add_matrices():
    size1, mat1 = matrix1()
    size2, mat2 = matrix2()
    if size1 == size2:
        result = []
        for row in range(int(size1[0])):
            result.append([])
            for el in range(int(size1[1])):
                result[row].append(float(mat1[row][el]) + float(mat2[row][el]))
        print_result(result, size1)
    else:
        print('Matrices must be the same size!')


def multiply_by_const(size=None, mat=None, c=None, auto=False):
    if not auto:
        size, mat = matrix1()
        c = float(input('Enter constant: '))
    result = []
    for row in range(int(size[0])):
        result.append([])
        for el in range(int(size[1])):
            result[row].append(float(mat[row][el]) * c)
    if auto:
        return result
    else:
        print_result(result, size)


def multiply_matrices():
    size1, mat1 = matrix1()
    size2, mat2 = matrix2()
    new_size = [size1[0], size2[1]]
    if size1[1] == size2[0]:
        result = []
        for row in range(int(size1[0])):
            result.append([])
            for col in range(int(size2[1])):
                res = 0
                for x in range(int(size2[0])):
                    res += float(mat1[row][x]) * float(mat2[x][col])
                result[row].append(res)
        print_result(result, new_size)
    else:
        print('Matrices must have proper sizes to multiply!')


def transpose(size=None, mat=None, auto=False):
    if auto:
        choice2 = '1'
    else:
        print('\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        choice2 = input('Your choice: ')
        size, mat = matrix1()

    if choice2 == '1':
        result = []
        for row in range(int(size[0])):
            result.append([])
            for col in range(int(size[1])):
                result[row].extend('0')
        for row in range(int(size[0])):
            for col in range(int(size[1])):
                result[col][row] = mat[row][col]
        if auto:
            return result
        else:
            print_result(result, [len(result), len(result[0])])

    elif choice2 == '2':
        result = []
        for row in range(int(size[0])):
            result.append([])
            for col in range(int(size[1])):
                result[row].extend('0')
        for row in range(int(size[0])):
            for col in range(int(size[1])):
                result[col][row] = mat[int(size[0])-row-1][int(size[1])-col-1]
        print_result(result, [len(result), len(result[0])])

    elif choice2 == '3':
        result = []
        for row in range(int(size[0])):
            mat[row].reverse()
            result.append(mat[row])
        print_result(result, size)

    elif choice2 == '4':
        result = []
        for row in range(int(size[0])-1, -1, -1):
            result.append(mat[row])
        print_result(result, size)

    else:
        print('Wrong option!')


def minor(mat, not_i, not_j):
    result = []
    temp_mat = mat[:not_i]
    try:
        temp_mat += mat[not_i + 1:]
    except IndexError:
        pass
    for i, i_v in enumerate(temp_mat):
        result.append([])
        for j, j_v in enumerate(i_v):
            if j != not_j:
                result[i].append(float(j_v))
    return result


def calculate_determinant(size, mat):
    if size[0] != size[1]:
        return "It's not a square matrix!"
    elif int(size[0]) == 1:
        return float(mat[0][0])
    elif int(size[0]) == 2:
        return float(mat[0][0]) * float(mat[1][1]) - float(mat[1][0]) * float(mat[0][1])
    else:
        det = 0
        minor_size = [float(size[0]) - 1, float(size[1]) - 1]
        for j, j_v in enumerate(mat[0]):
            det += (float(j_v) * (-1) ** j * calculate_determinant(minor_size, minor(mat, 0, j)))
        return det


def inverse_matrix():
    size, mat = matrix1()
    minor_size = [int(size[0]) - 1, int(size[1]) - 1]
    det = calculate_determinant(size, mat)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return
    c = []
    for i, i_v in enumerate(mat):
        c.append([])
        for j, j_v in enumerate(i_v):
            m = minor(mat, i, j)
            minor_value = ((-1) ** (i + j)) * calculate_determinant(minor_size, m)
            c[i].append(minor_value)
    c_tr = transpose(size, c, True)
    factor = (1 / det)
    result = multiply_by_const(size, c_tr, factor, True)
    print_result(result, size)


def print_result(result, size):
    print('The result is:')
    for row in range(int(size[0])):
        for el in range(int(size[1])-1):
            print(result[row][el], end=' ')
        print(result[row][int(size[1])-1])


while True:
    print(f'\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices'
          f'\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    choice = input('Your choice: ')
    if choice == '0':
        break
    elif choice == '1':
        add_matrices()
    elif choice == '2':
        multiply_by_const()
    elif choice == '3':
        multiply_matrices()
    elif choice == '4':
        transpose()
    elif choice == '5':
        print(calculate_determinant(*matrix1()))
    elif choice == '6':
        inverse_matrix()
    else:
        print('Type in proper answer')
