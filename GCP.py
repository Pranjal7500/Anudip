num1 = int(input("Enter a number"))
num2 = int(input("Enter second number"))

condn = min(num1,num2)
divisor = 1
gcp = 1
while divisor <= condn:
    if num1%divisor==0 and num2%divisor==0:
        gcp = divisor
    divisor +=1

print("The GCP is:",gcp)