import math
from re import I

# a = 5
# print("a={a}; {b} {c}".format(a=a, b="b", c="c"))
# b = 10.5
# a = a + b
# a = math.floor(a)
# print(a)
# a = "s" + str(5) # "5"
# print(a)

# age = 35
# if age >= 20:
#     print(">=20")
# else:
#     print("<20") 

# sum = 1
# for i in range(1,101,1):
#     sum = sum * i
# print(sum)

# # list
# books = [5, "abc", 10.0, True]
# print(books[-1])
# for book in books:
#     print(book)

def add(a, b):
    return a + b
print(add(1, 2))

def factorial(c):
    j = 1
    for i in range(1, c+1, 1):
        j = j * i 
    return j
print(factorial(4)) 


class MyAwesomeClass:

    def __init__(self, number, s1, s2):
        self.number = number
        self.s1 = s1
        self.s2 = s2

    def show(self):
        print("{a} {b} {c}".format(a=self.number, b=self.s1, c=self.s2))

# object1 = MyAwesomeClass(10, "a", "b")
# object1.show()

# object2 = MyAwesomeClass(100, "aaa", "bbb")
# object2.show()
