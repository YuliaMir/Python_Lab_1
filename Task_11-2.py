'''Дан файл с расширением .txt, содержащий в каждой строчке
следующую информацию: номер, фамилия, имя, компания,
зарплата, разделенные запятыми.
Создайте Эксельный файл, в который перенесите эту информацию,
предварительно отсортировав этот список по компании, по
фамилии и имени.
В конце списка добавьте строку: ИТОГО и суммарное значение всех
зарплат.'''


with open('input.txt', 'r') as file:
    lines = file.readlines()

sorted_lines = sorted(lines[1:], key=lambda x: (x.split(',')[3], x.split(',')[1], x.split(',')[2]))
total_salary = sum(float(line.split(',')[4]) for line in sorted_lines)
total_row = f'ИТОГО,,,{total_salary}\n'
sorted_lines.append(total_row)

with open('employees.xlsx', 'w') as file:
    file.write(lines[0])
    file.writelines(sorted_lines)

print("Отсортированные данные доступны в файле")
