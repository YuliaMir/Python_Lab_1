'''Напишите функцию, которая на вход получает DataFrame, который
содержит числа и строки, а в качестве результата возвращает
сумму всех чисел.'''

import pandas as pd


def sum_of_numbers_in_dataframe(df):
    total_sum = 0

    for column in df.columns:
        for value in df[column]:
            if isinstance(value, (int, float)):
                total_sum += value

    return total_sum


data = {'A': [1, 'almond', 3.5],
        'B': ['bread', 6, 4],
        'C': [5, 'coffee', 76]}
df = pd.DataFrame(data)

result = sum_of_numbers_in_dataframe(df)
print(f"Сумма всех чисел в датафрейме: {result}")
