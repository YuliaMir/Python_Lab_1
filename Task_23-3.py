'''Создайте функцию, на вход которой подается список из целых положительных
чисел, и которая в качестве результата возвращает самое большое число,
которое можно составить из этих чисел.
Например, вход [1, 21, 3], результат 3211
Если вход [9, 81, 25], то результат 98125.'''


def largest_number(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    return int(''.join(numbers))

input1 = [0, 21, 3, 7]
result1 = largest_number(input1)
print(f"Input: {input1}, Result: {result1}")

input2 = [8, 81, 250]
result2 = largest_number(input2)
print(f"Input: {input2}, Result: {result2}")
