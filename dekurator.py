#Теорія декораторів
import time
def my_decorator_func(func):#3
    def wrapper():
        print('Щось там')
        func()
        print('І там шось')
    return wrapper

@my_decorator_func #2
def say_hello(): #Крок 1
    print('Hello!')
say_hello()


def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper



@delay_decorator
def sleepy():
    print('Я сплю')
sleepy()


def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n], cache
    return wrapper
@cache_decorator
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))