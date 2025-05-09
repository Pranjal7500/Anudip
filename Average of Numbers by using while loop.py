#WAP to take five number as input find  the average of the number

i = 1
sum = 0
while i<=5:
    n = int(input("Enter number:"))
    sum = sum+n
    i+=1
print("Average =",sum/5)
