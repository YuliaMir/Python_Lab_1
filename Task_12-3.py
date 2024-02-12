'''Напишите функцию, которая на вход принимает строку диапазонов
натуральных чисел,
например: ‘1-2,4-4,3-6’.
На выходе функция должна сформировать список натуральных
чисел, которые попадают в один из этих диапазонов,
например: [1,2,4,3,4,5,6].'''


def generate_numbers_from_ranges(range_string):
    ranges = range_string.split(',')
    result = []

    for r in ranges:
        start, end = map(int, r.split('-'))
        result.extend(range(start, end + 1))

    return result


range_string = '1-2,4-4,3-6'
output_list = generate_numbers_from_ranges(range_string)
print(output_list)
