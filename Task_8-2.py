'''Сортировка списка, состоящего из списка чисел'''

lst = [[1,4], [44,16,7,25], [5,7,8]]

def sort_key(sublist):
    return (sum(len(str(num)) for num in sublist), sublist)

sorted_lst = [sorted(sublist, reverse=True) for sublist in sorted(lst, key=sort_key)]

print(sorted_lst)






