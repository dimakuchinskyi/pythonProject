#Лабороторна робота
#1

def decor_plus_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper
@decor_plus_10
def my_func(x):
    return x
result = my_func(int(input('Введіть число: ')))
print(result)















