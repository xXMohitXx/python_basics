def hello():
    print('thia is a function in python')
hello()

#parameterised functions
def sum(x,y):
    s = 0
    for i in range(x,y+1):
        s = s + i
    print('Sum of integers from', x, 'to', y, 'is', s)

x = eval(input('Enter a number to start the range from:- '))
y = eval(input('Enter a number to end the range:- '))
sum(x,y)