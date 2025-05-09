
#WAP to take a number as input and print the table of the number
n = int(input("Enter number: "))

def table(n): 
    i = 1
    while i <= 10:
        print(f"{n} * {i} = {n * i}")
        i += 1


table(n)