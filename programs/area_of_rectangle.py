#area of rectangle using user input
print('Enter the length of rectangle')
#len = input(int) # this will take input in the form of a string so do this :-
len = int(input())
print('Enter the breadth of rectangle')
bre = int(input())
ans = len * bre
print('the area of rectangle is ', ans)

'''bonus
type conversion from str to int'''

print('please enter number')
num1 = input()
print('num1 = ', num1)
print(type(num1))
print("Converting type of Num1 to int")
num1 = int(num1)
print(num1)
print(type(num1))