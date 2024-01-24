'''Напечатать спираль из чисел'''

n = int(input())

matrix = [[0] * n for i in range(n)]

number = 1
row, col = 0, 0
direction = 0


for i in range(n * n):
    matrix[row][col] = number

    if direction == 0:
        if col == n - 1 or matrix[row][col + 1] != 0:
            direction = 1
            row += 1
        else:
            col += 1
    elif direction == 1:
        if row == n - 1 or matrix[row + 1][col] != 0:
            direction = 2
            col -= 1
        else:
            row += 1
    elif direction == 2:
        if col == 0 or matrix[row][col - 1] != 0:
            direction = 3
            row -= 1
        else:
            col -= 1
    elif direction == 3:
        if row == 0 or matrix[row - 1][col] != 0:
            direction = 0
            col += 1
        else:
            row -= 1

    number += 1


for row in matrix:
    for number in row:
        print("{:2d}".format(number), end=" ")
    print()
