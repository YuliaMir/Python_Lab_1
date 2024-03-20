'''Напишите функцию, которая сравнивает две строки и выдает True,
если между ними есть не более, чем 1 разница в буквах, и False во
всех остальных случаях. Если две строки равны, то True.
Например:
‘abc’ и ‘abc’ – True, ‘abc’ и ‘abcd’ – True,
‘bc’ и ‘abc’ – True, ‘axc’ и ‘abc’ – True
‘abc’ и ‘acb’ – False, ‘abc’ и ‘a’ – False, ‘’ и ‘ ‘ - False'''

def compare_strings(str1, str2):
    if str1 == str2:
        return True

    if abs(len(str1) - len(str2)) > 1:
        return False

    diff_count = 0
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            diff_count += 1

            if len(str1) > len(str2):
                i += 1
            elif len(str2) > len(str1):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

        if diff_count > 1:
            return False

    if i < len(str1) or j < len(str2):
        diff_count += 1

    return diff_count <= 1

print(compare_strings('abc', 'abc'))
print(compare_strings('abc', 'abcd'))
print(compare_strings('bc', 'abc'))
print(compare_strings('axc', 'abc'))
print(compare_strings('abc', 'acb'))
print(compare_strings('abc', 'a'))
print(compare_strings('', ' '))



