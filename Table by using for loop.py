#WAP to take a number as input and print the table of the number by using for loop

n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")