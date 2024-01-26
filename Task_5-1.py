'''Ввести число n. Напечатать треугольник Паскаля. '''

n = int(input())
x = []

for i in range(0, n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = x[i - 1][j - 1] + x[i - 1][j]

    x.append(row)

for z in x:
    print(z)