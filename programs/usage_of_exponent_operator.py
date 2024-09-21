#here we will find the distance between two points
print('Point 1')
x1 = eval(input('Enter the co-ordinates of x = '))
y1 = eval(input('Enter the co-ordinates of y = '))

print('Point 2')
x2 = eval(input('Enter the co-ordinates of x = '))
y2 = eval(input('Enter the co-ordinates of y = '))

len = (x2 - x1) ** 2 + (y2 - y1) ** 2
ans = len ** 0.5

print('the length between point1 and point 2 is = ', ans)

#with the help of this we can solve all the basic equations