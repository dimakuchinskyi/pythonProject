#Класна робота
#Теорія
#1
'''
def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)

black_hole(234, 'Earth', 'rusnya', 'time', 6776)
'''
#2
'''
def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for argument in kwargs:
        print(argument)
black_hole_named(name='Gleb', planet='Xleb', number = 5)
'''
#3
'''
def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
black_hole_named(name='Gleb', planet='Xleb', number = 5)
'''
#4
'''
def black_hole_full(*args, **kwargs):
    if not args: #Для переірки наявності не іменнованих аргументів
        return 0
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(key, value)
black_hole_full('Earth', 'rusnya', 'time', 6776, name='Gleb', planet='Xleb', number = 5234)
'''
#5
'''
lst = [2, 3, 4]
dict = {'1':1, '2':2, '3':3 }
def fun(var_1, var_2, var_3):
    print(var_1. var_2, var_3)
fun(*lst)
'''
#6
'''
def fun_dict(n, b, n1):
    print(1, 2 ,3)
fun_dict(**dict)
'''
#Лабораторна робота
#1
'''
def average(*args):
    return sum(args)/ len(args)
print(average(15 ,344, 545535, 57, 55, 8566))
'''
#2
'''
def max_lenght(*args):
        if not args:
            return 0
        return len(max(args))
print(max_lenght('fdtjyjydtjyd', 'fhd', 'htrhhtr'))
'''
#3
'''
def vsi(**kwargs):
    return ' '.join(kwargs)
print(vsi(lox='Maks', name='Dima', palnet='Earth', pet='38M «Толди» (венг. 38M Toldi)'))
'''
#4
people = [('Gleb', 17), ('Max', 5), ('Dima', 24)]
def create_dict(*args, **kwargs):
    age_dict = {}
    for name, age in people_lsit:
print(create_dict(people))































