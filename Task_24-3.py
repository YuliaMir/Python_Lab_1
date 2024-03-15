'''Создайте функцию, которая принимает на входе строку из открывающих и
закрывающих круглых скобок.
Функция возвращает False, если число скобок "(" не равно числу скобок ")".
Функция возвращает True, если в любой подстроке, начинающейся с начала, число
скобок ")" не превышает число скобок ")".
Функция возвращает False во всех остальных случаях.
Примеры:
"()" => true
")(()()" => false
"(" => false
"(()) (( () () ) () )" => true
"())(()" => false'''


def check_brackets(input_str):
    open_count = 0
    close_count = 0

    for i in range(len(input_str)):
        if input_str[i] == '(':
            open_count += 1
        elif input_str[i] == ')':
            close_count += 1

        if open_count < close_count:
            return False

    return open_count == close_count


test_cases = ["()", ")(()()", "(", "(())((()())())", "())(()", ")", ""]
for test_case in test_cases:
    print(f'Input: "{test_case}" => Output: {check_brackets(test_case)}')
