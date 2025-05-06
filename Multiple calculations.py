#wap to take 2 number as input and create basic calculator for it

num1 =int(input("Enter a number:"))
num2 = int(input("Enter second number"))
o = input("Enter an operator")
if o == '+':
    print("Sum =",num1+num2)
elif o =='-':
    print("Subtraction =",num1-num2)
elif o =='*':
    print("Multiplication =",num1*num2)
elif o =='/':
    print("Divide =",num1/num2)
else:
    print("Error! Invalid operator")