'''Напишите функцию, которая сортирует числовой список, не
используя никаких функций, вроде sort, sorted, max, min и т.д.'''


def sort_list(lst):
    sorted_list = []

    while lst:
        minimum = lst[0]
        for num in lst:
            if num < minimum:
                minimum = num
        sorted_list.append(minimum)
        lst.remove(minimum)

    return sorted_list


my_list = [4, 2, 7, 1, 3, 0, 100, 1.5, -1]
sorted_list = sort_list(my_list)
print(sorted_list)
