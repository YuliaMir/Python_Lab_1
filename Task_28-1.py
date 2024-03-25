'''Дан список чисел a. Назовем пару (а[i], a[j]) инверсией, если i < j, а
а[i] > a[j]. Напишите функцию, которая возвращает количество
инверсий в списке.
Например:
[1,2,3,4,5] -> 0
[5,4,3,2,1] -> 10'''

def count_inversions(lst):
    inv_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                inv_count += 1
    return inv_count


print(count_inversions([1, 2, 3, 4, 5]))
print(count_inversions([5, 4, 3, 2, 1]))
print(count_inversions([5, 4, 3, 0, 1]))
print(count_inversions([0]))