'''Дан список, который состоит из одинаковых чисел за исключением одного.
Найдите это число.'''


def find_unique_number(nums):
    unique_nums = set(nums)

    for num in unique_nums:
        if nums.count(num) == 1:
            return num


nums = [2, 2, 1, 2, 2]
unique_number = find_unique_number(nums)
print(unique_number)


