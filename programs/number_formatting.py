x = 12.389932
print(x)
print(format(x," .2f")) #you have to use the format function along with the print statement else it will not work

#formatting floating point integerswith different values

print(format(10.345, "10.2f"))
print(format(10, "10.2f"))
print(format(10.32245, "10.2f"))

#here the 10 is the field width, 2 is the precision of the decimal points and f is the conversion code

#justification of formats
print(format(10.22345, "10.2f")) # this is the right justification
print(format(10.22345, "<10.2f")) #this is left justification format

#string formatting
print(format("hello brother", "5s")) #in string s is used as the conversion code

#formatting as a percentage
print(format(10.345, "10.2%")) #here the value is automatically multiplied by the value of 100 to give percentage
print(format(0.10345, "10.2%")) #10.35%

#there is also scientific notation but it is also used as the same format just use the conversion code e for it
