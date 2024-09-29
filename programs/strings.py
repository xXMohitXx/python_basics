s1= "Python"
print(s1[0]) #this is to access the first element of the string

#accessing the string via negative indexes
print(s1[-2])
print(s1[::-1]) #will print the reverse of the string

#to display length of the string
print(len(s1)) #6

#string traversing using for loop
for ch in s1:
    print(ch,end="")
print()
#using while loop
index = 0
while(index<len(s1)):
    print(s1[index],end="")
    index+=1
print()

#example of immutable strings
str1= "I am Mohit"
#str1[0] ="U" #will throw error
#print(str1)
# so to make changes we can make a new string itself
str2 = "U"+str1[1:]
print(str1,str2)

#string ids
print(id(str1))

#string slicing
S="hello brother"
print(S[4:10]) # it means index 4 is the starting point and will print all characters before index 10

#sting slicing but with steps size
print(S[0:len(S):2]) #start index till the length of the string with step 2
#more examples
print(S[::]) #entire string
print(S[::-1])#reverse
print(S[-1:0:-1]) #will reverse but wont display the 1 index
print(S[:-1]) # wont display the -1 index

# the + and * operators
S1 = "Hello"
S2 = " bro"
print(S1+S2) #Hello bro
print(3*S1) #HelloHelloHello

# The in and not in operators
S1 = "Computer Science"
print("Science" in S1) #true
print("Technology" in S1) #false
print("Science" not in S1) #false
print("Technology" not in S1) #true

#String comparison
S1 = "abc"
S2 = "abc"
print(S1 == S2) #true

S1 = "ABC"
S2 = "DEF"
print(S1 > S2) # False (will check ascii values)

S1 = "ABCD"
S2 = "abcd".upper()
print(S1 > S2) #FALSE
print(S1 >= S2) #true

#the .format() method
print("my name is {0} and im from {1}".format("Mohit","Kutch"))

#the split() method
#it will make list
Str = "Python Javascript PHP JAVA C"
print(Str.split())
#there are many string operations such as capitalize isupper islower upper lower title swapcase strip count rfind find endswith startswith isspace isdigit isalnum isalpha that you can try it ou