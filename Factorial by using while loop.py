#WAP to take  anumber as input and find  factorial of the number

n = int(input("Enter the number: "))
i = 1
Factorial = 1

while i <= n:
    Factorial *= i
    i += 1

print(f"Factorial of {n} is: {Factorial}")
