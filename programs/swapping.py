#swapping of two variables
p = 3
q = 8
#using temp variable
temp = p
p = q
q = temp
print('first p = 3 and q = 8, now p = ', p, 'and q = ', q)

#without using temp variable

print('this method is called muliple assingments')
p, q = q, p
print('first p = 8 and q1 = 3, now p = ', p, 'and q = ', q)