import math
a = 5
b = 10.5
c = math.floor(b) # result: c=10.0 / result of "math.ceil" is 11.0
print("a={a}; b={b}, c={c}".format(a=a, b=b, c=c)) # result: a=5; b=10.5, c=10.0
print("a={a}; {b} {c}".format(a=a, b="b", c="c")) # result: a=5; b c
d = "s" + str(5) 
print(d) # result: s5

# Conditionals: if & elif & else
x = 1
y = 1
if x > y:
    print("x > y")
elif x < y:
    print("x < y") 
else:
    print("x = y")

# Loop
sum = 0
sumsum = 0
for i in range(1,101,2): # start from 1 to 100, step = 2 
                        # if set range(100), meaning start from 0 to 99, step =1
    sum = sum + i # option 1 to add up
    sumsum += i # option 2 to add up
print(sum)
print(sumsum)









