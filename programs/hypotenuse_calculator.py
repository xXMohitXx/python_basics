import math
base = eval(input('Enter base value ='))
height = eval(input('Enter height value ='))

sum1 = (base * base) + (height * height) #pythagoras theorem
ans = math.sqrt(sum1)

print('the hypotenuse value of triangle is =', ans)

