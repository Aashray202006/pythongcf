#sets in python 
#Not ordered(no index value), partially mutable(modified by methods)
#unique elements (they dont allow duplicates)

b={1,2,3,4,5,6}
c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
print(b)
print(type(b))

# -> Add

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)

# -> Remove

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)
c.remove("add") #removes the element from the set

c={1,1,2,3,7,1,12,844,7,55,7,51,5754,774,2,21,1}
print(c)
c.add("add") #adds the element in the set
print(c)
c.remove("add") #removes the element from the set
# c.remove("add") #-->key error :- removing the same element from the set
c.discard("add")  

# -> Empty set 

emset=set() #creating empty set
print(emset)
print(c)

# -> Boolean method

c={1,2,85,285,52254,2,50,25,0,24,14,22,41,24,25,50,7}
print(c)
print(10 in c) #if the value is present in the set then output is true else false

# -> update
b={5,5,25,45,4,2,5,1,5532,65,54}
c={1,2,85,285,52254}
print(c)
c.update(b) # adds a set in the set(UPDATES MULTIPLE ELEMENTS)
print(c)

# -> clear

c={1,2,85,285,52254}
print(c)
c.clear() # clears out all the elements in the sets 
print(c)

# -> Copy

b={1,2,85,285,52254}
e=b.copy()  # creates a duplicate copy of the element
print(e)

#union(|) = combines both set and duplicates will be considered as single value

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element

print(A.union(B))
print(A|B)

#Intersection(&) = elements which are present in A and B (Common elements)

A = {1, 2, 7, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.intersection(B))
print(A&B)



A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.difference(b)) #Elements which are in "A" but not in "B"
print(A-B)

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(B.difference(A)) #Elements which are in "B" but not in "A"
print(B-A)

A = {1, 2, 7, 4}
B = {5, 6, 7, 8}
#Two methods to print the element
print(A.symmetric_difference(B)) #symmetric_difference(^) = elements which are not in "A" and "B"
print(A^B)

#Frozen set after created a set, changing the value or update the value in not possible

x=frozenset([1,2,3,4,5,6]) #immutable even via methods
print(x)  #->Attribute error
# x.add(7) # as frozen set is completely imutable so they cant be modified

#--> Dictionary ={key : value, key : value, key : value}
# unorderd , cannot have duplicates in key
# mutable
# Fast lookups using keys
#python dictionary -> '' or ""
#json-->""
a = { "Name":"Aashray","Surname" : "Shah" ,"student": True ,"Age": 20} 
print(a)
#we can change the value by the keywords
a["Name"]="Unknown"
print(a)
a["Surname"]="Not Known"
print(a)
a["student"]=False
print(a)
b={"student" :"Falcon" ,"Age":25 ,"Other_Student" : { "Name": "mischelle","Age":22}}
print(b["Other_Student"]["Name"])
#updates the value of one dictionary from another
a.update(b) #updates the value of 'a' with key-value pairs from 'b'
print(a) # Print 'a' after the update to see the changes

a = { "Name":"Falcon","Surname" : "Denver" ,"student": True ,"Age": 20} 
b = { "Name":"mischelle","Surname" : "River" ,"student": True ,"Age": 25} 
c = { "Name":"","Eren" : "Eager" ,"student": True ,"Age": 20} 
#to print all the key from the dictionary
for i in a.keys():
    print(i)
#to print all the values from the dictionary
for i in a.values():
    print(i)
# to print all the key and values from the dictionary
for k,v,in a.items():
    print("key= "+k)
    print("Value = "+str(v))

#STRINGS IN PYTHON

#multiline string
a='''Hey
Are 
You 
There'''
print(a)
#accesing the character via index from a string
#index value are similar to that of list (start from 0)
B="gsgdfusaudasu"
print(B[2])
print(B[-1])#last element also had -1 index value if start from reverse
print(B[1:4])#slice method 
c="abcdefghijklmnopqrstuavwxyzaa"
print(c[-9:-4])

print(B.upper()) #gives the value of string in upper case
#similary for lower case print(B.lower())
c=" abcdefghijklmnopqrstuavwxyzaa"

print(c.strip()) # removes the space from the string 
print()
print(c.replace( "a", "A")) #replace the value to replaced with given value
#              replace ,by 
B="g,s,g,d,f,u,s,a,u,d,a,s,u"

d=B.split(",")# coverts string to list
print(d)
print(type(d))

c="a b c d e f g h i j k  l m n op q r s t u a v w x y z a a"
e=c.split(" ")#here they are seperated by space. in line 55 they are divided by comma
print(e)
print(type(e))
print("*".join(e))#converts list to string (here diffrent symbols can also be used instead of"*")

f="dsadasdasd"
print(f.startswith("d")) #gives boolean value 
print(f.endswith("d"))  #gives boolean value whether true or false
print(f*3) # string will get multiply 3 times 
print("A" in f) #to check whether the element is present or not

# input from user (terminal>new terminal >(write)python filename.py))
# a=  int(input("enter the number A = ")) # input take the value in string 
# b = int(input("enter the number b = ")) 
# print("the addition is =",(a+b))
# print("the subtraction is = ", (a-b))
# print(f"the multiplication is = {a*b}")#string formatting
# print(f"the division is = {a/b}")
# print(f"the modulus operation is = {a%b}")

## email validator(Basic) ##

# email=input("Enter your email :")
# if "@" in email and email.endswith(".com"):
#     print("Valid email")
# else:
#     print ("Invalid email")

# if statement 
age=int(input("Enter your age =" ))
if age>=27:
    print("You Are Eligible")
#  if else statement
age=int(input("Enter your age =" ))
if age>=27:
    print("You Are Eligible")
else:
    print("You Are Not Eligible")
    
