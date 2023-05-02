
#1
def sum_list(lst):
     return sum(lst)
numbers = [1,2,3,4,5,6,7,8,9,10]
sum_numbers = sum_list(numbers)
print(sum_numbers)
#2
def palindrom(s):
    if s == s[::-1]:
                    print("True")
     else:
        print("False")
s = input("Введіть текст:")
palindrom(s)
#3
def sort_len(lst):
     return sorted(lst, key = len)
slova = ["Banana","Bakhmut","Leopard","Car","Dima","Simferopol"]
sorted_slova = sort_len(slova)
print(sorted_slova)