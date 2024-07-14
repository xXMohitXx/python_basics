num1 = eval(input('Enter number 1 = '))
num2 = eval(input('Enter number 2 = '))
num3 = eval(input('Enter number 3 = '))

if num1 > num2:
    if num2 > num3:
        print(num1, "is greater than ", num2, "and", num3)
else:
    print("num1 is not bigger than num2 and num3")
