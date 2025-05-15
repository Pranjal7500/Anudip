st = 'Poonam'
print(st[3])

# string slicing
print(st[2:6])
print(st[2:6:2])
print(st[2:])
print(st[:5])
print(st[::])
#Functions
print(len(st))
print(st.upper())
print(st.lower())
print(st.swapcase())




name = "Pranajl"
age = '21'
print("My name is {} and  i am {} years old.".format(name,age))

#WAP to take sting as input and reverse the string

str = input("Enter the string: ")
print("Reverse String :",str[::-1])




#WAP a Program to take  a string as a input and count the number of vowels

str = input("Enter the string:")  # Enter  the string
vowels = "aeoiuAEOIU"    #vowles definr
count = 0
for char in str:          # taken for loop for 
    if char in vowels: # if voewls are present in string then i just count it
        count +=1
    print(f"The string contain {count} vowels.") # print the final stetemnt and count for the vowels.



    
    
  #WAp a program to remove a newline in Python String   
  
line = "\nBest \nDeeptech \nPython \nTraining\n"
print = line.replace("\n","")
