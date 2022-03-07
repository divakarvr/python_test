import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
if num1 < num2:
    num1, num2 = num2, num1
ans = eval(input("what is " + str(num1) + "-" + str(num2) + " : "))


if num1 - num2 == ans:
    print( "you are correct")
else:
    print( "Wrong the subraction of ", str(num1), "-", str(num2), "is", num1-num2, ".")

