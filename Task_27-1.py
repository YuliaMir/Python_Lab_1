'''
Введите число n от 1 до 18.
Напечатайте квадратную матрицу, имитирующую Дартс.
Например для n = 5.
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1'''


def create_darts_layout(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = max(abs(i - n // 2), abs(j - n // 2)) + 1

    max_number = max(map(max, matrix))
    max_digits = len(str(max_number))

    for row in matrix:
        print(' '.join(str(max_number - cell + 1).rjust(max_digits) for cell in row))


n = int(input("Введите число от 1 до 18: "))
create_darts_layout(n)