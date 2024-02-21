'''Создайте декоратор, который переводит результат функций в нижний регистр.'''

def lowercase_deco(func):
    def wrapper():
        origin_result = func()
        modi_result = origin_result.lower()
        return modi_result
    return wrapper

@lowercase_deco
def h():
    return 'HELLO'
print(h())