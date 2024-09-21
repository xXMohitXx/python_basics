'''
the eval is used to evaluate. it will take string as a parameter and will return as a python expression

it takes string and return it in the type in which the entered string is expected
using it we do not require to explicitly type convert the code for integer and float values

'''
name = input('Enter name')
age = eval(input('Enter age'))
gender = input('Enter gender')
height = eval(input('Enter Height in foot'))

print('USER DETAILS ARE AS FOLLOWS')
print('Name ', name)
print('Age ', age)
print('Gender ', gender)
print('Height ', height)