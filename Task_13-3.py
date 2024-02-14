'''Создайте функцию-генератор, который принимает в качестве
аргумента список целых чисел, а в качестве результатов формирует
последовательность нечетных чисел из этого списка.'''

def odd_numbers_from_list(input_list):
    for num in input_list:
        if num % 2 != 0:
            yield num

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen = odd_numbers_from_list(input_list)

for odd_num in gen:
    print(odd_num)
