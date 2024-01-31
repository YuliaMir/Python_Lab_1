'''Дан x - двумерный массив чисел в виде списка содержащего строки в виде списков. Размер массива n - строк, m - столбцов.
Напишите функцию которая принимает этот массив как аргумент и в качестве результата отдает отсортированный список трех самых больших чисел. '''

x = 2
y = int(input())

matrix = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(j)
    matrix.append(row)
print(matrix)
def define_largest_numbers(matrix):
    largest_numbers = [float('-inf'), float('-inf'), float('-inf')]
    for row in matrix:
        for num in row:
            if num > largest_numbers[0]:
                largest_numbers = [num, largest_numbers[0], largest_numbers[1]]
            elif num > largest_numbers[1]:
                largest_numbers = [largest_numbers[0], num, largest_numbers[1]]
            elif num > largest_numbers[2]:
                largest_numbers = [largest_numbers[0], largest_numbers[1], num]
    return sorted(largest_numbers)

print(define_largest_numbers(matrix))

