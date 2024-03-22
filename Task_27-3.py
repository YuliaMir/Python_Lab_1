'''Дан список.
Посчитайте сколько в нем элементов, включая вложенные списки.
Например:
[] --> 0
[1, 2, 3] --> 3
["x", "y", ["z"]] --> 4
[1, 2, [3, 4, [5]]] --> 7'''

def count_elements(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_elements(item)
        count += 1
    return count


test_case = [1, 2, [3, 4, [5]]]

result = count_elements(test_case)
print(f"{test_case} --> {result}")








