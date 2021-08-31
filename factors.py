def myfunc(num1, num2):
    if num1 % num2 == 0:
        print("num2 is a factor of num1")
    elif num2 % num1 == 0:
        print("num1 is a factor of num2")
    else:
        print("numbers are not factors")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

myfunc(num1, num2)