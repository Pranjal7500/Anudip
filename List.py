#list = [10,20,30,'poonam','pranjal','porje']
#print(list[2])

#List slicing
#print(list[1:4])
#print(list[1:2:3])
#(list[:2])
#print(list[::])
#list[2] =33
#print(list)
#list.append(19)  # add element to last list
#print(list)
#list.insert(1,34) # add element in list anywhere
#print(list) 
### POP is used to pop the element or remove the element from the list where we specified

#b = ['Apple','Banana','Grapes']
#list.extend(b)
#print(list)
#print(list.index('Apple'))# to know the index of element
#print(list.count('Apple')) # how many times that index has occured

#l = [2,5,7,9,10,13,33,45]
#l.sort()
#print(l)
#l.reverse()
#print(l)


#List Comprehension
#n = [i+5 for i in l]
#print(n)

#wap to create a cube value list of below list using list comprehension

#l = [10,20,30,40,7]
#n = [i*i*i for i in l]
#print(n)

#Enumerate Method  :: used to show both index and value/element in the list

#for  i,v in enumerate(l):
 #   print("index :",i,"value : ",v*v)



#while loop
#i = 0
#while i<len(l):
 #   print(l[i])
  #  i +=1

#WAP program to get the largest and smallest number from a list without built function

#l = [9,23,455,33,19191,20000]
#s = l[0]
#for i in l:
 #   if i <=s:
            #s=i
#print("Smallest number is :",s)

#large= l[0]
#for i in l:
 #   if i >=large:
  #       large=i
#print("Largest numbernumber is :",large)

#Wap to find duplicate values from a lsit and diaplay those

l = [12,3,12,56,76,56]
d = []
for i in l:
     if l.count(i) >1:
          if i not in d:
                d.append(i)
print(d)


