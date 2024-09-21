def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(int(input("Enter the number which you want factorial of:- "))))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter number of terms to display fibonacci series:- "))

if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))