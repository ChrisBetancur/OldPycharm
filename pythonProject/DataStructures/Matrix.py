import random

MAX = 5
MIN = 0


def init_matrix(matrix, num_of_rows, numb_of_columns):
    for rowIndex in range(num_of_rows):
        row = []
        for columnIndex in range(numb_of_columns):
            row.append(random.randint(MIN, MAX))
        matrix.append(row)
    return matrix


def is_contains_value(matrix, value):
    if matrix is not None:
        for row in matrix:
            for curr_value in row:
                if curr_value == value:
                    return True
    return False


def delete_value_from_matrix(matrix, value):
    if is_contains_value(matrix, value) is False:
        return

    row_counter = 0
    for row in matrix:
        col_counter = 0
        for curr_value in row:
            if curr_value is value:
                matrix[row_counter][col_counter] = 0
            col_counter += 1
        row_counter += 1
    return matrix


def print_array(arr):
    if arr is not None:
        for row in arr:
            for value in row:
                print(value, ", ", end='')
            print()


arr = []

init_matrix(arr, 4, 4)

print_array(arr)
print()
delete_value_from_matrix(arr, 4)
print_array(arr)
