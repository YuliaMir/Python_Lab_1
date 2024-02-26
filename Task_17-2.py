'''Создайте декоратор, которые переводит все текстовые аргументы функции в
верхний регистр и возвращает их в виде списка текстовых аргументов.
Текстовые аргументы – это строки в args и строковые значения в kwargs.'''


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        args = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        kwargs = {key: value.upper() if isinstance(value, str) else value for key, value in kwargs.items()}

        return func(*args, **kwargs)

    return wrapper


@uppercase_decorator
def example_function(*args, **kwargs):
    return list(args) + list(kwargs.values())


# Example usage
result = example_function("hello", "world", name="Ivan", age=22)
print(result)
