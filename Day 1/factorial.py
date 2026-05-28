def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact
n = int(input("Enter a number: " ))
if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("The factorial of ",n,"is", fact(n))