#write a program to find whether the given number is prime or not
num = eval(input('Enter a number to find if it is prime or not = '))
flag = 0
for i in range(2,num):
    if num % i == 0:
        flag = 0
        break
    else:
        flag = 1
if flag == 1:
    print("The value is prime")
else:
    print("The given value is not prime")