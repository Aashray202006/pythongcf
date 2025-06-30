#output

print("Hello World")
print(True)
print(15)

#index 
e=[1,2,5,15,5546764456]
#  0,1,2,3,4,5 value of index
e=[1, 2, 5]
# -3,-2,-1
#index from last element (last element had index number -1)

#function 

def greet(a): #defining a function #a-->parameter
    print("hello world" +a)

greet(" Here we go") #function calling #Here we go -->argument

name="admin" #global scope variable can be acces by all the function

def add(a,b):
    addition="to add" #local variable and can be acces by the function it is been defined
    print(a+b)

add(5,6)
def mul(b,c):
    print(b*c)

mul(5,9)
def sub(d,e):
        print(d-e)

sub(5,7)
def div(e,f):
    print(e/f)

div(5,6)
def expo(g,h):
    print(g**h)

expo(5,6)
def mod(i,j):
    print(i%j)

def add(a,b):
    return(a+b)
print(add(5,6)+add(1,3))

print(name)

#type function gives the datatype

a=12
b="HelloWorld" 
c=True
d=2.225
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#list symbol=[]

e=[1,3,"Hey",True]
print(type(e))
print(e)
print(e[3]) #accesing via index
e[3]="Byee!"#modifying via index
print(e[3])
print(e[-1])#index in reverse order start with -1 means that last value of index will have index -1 in reverse order then-2,-3,..so on
print(e[-2])

#append -->adds element at last position in the list
e.append(1000)
print(e) 

#index --> gives the index value of element
print(e.index("Hey"))

#extend --> combine two list ( list e is combined with list f )
f=[1,2,3,4,5]
e.extend(f)
print(e)

#remove --> removes an element in list
e.remove(5)
print(e)
#pop-->removes last element when no argument is given and removes a element at argument position when passed
e.pop()
print(e)
#clear--> clear all the element
g=[1,2,3]
print(g)
g.clear()
print(g)
#slice method-->[start:stop-1]
e=[1,3,"Hey",True,2145,352,65151]
print(e[1:3])

#reverse method-->gives the element in reverse order
e.reverse()
print(e)

# the value of function here is 100 and the value inside the function is "hey"
def greet():
     print("Hey")
     return 1000
print(greet())

#sort-->orders the element in ascending order
e=[1,2,5,15,5546764456]
print(e)
e.sort()
print(e)
e=[1,2,5,15,5546764456]

g=e
g.pop()
print(g)
print(e)
#shallow copying -->elemnt of a list is copied and assingned to another variable  
g=e.copy()#creates duplicate
g.pop()
print(g)
print(e)
#insert-->insert(index,value)-->adds an element u=in given index in a list
e=[1,2,5,15,5546764456]
print(e)
e.insert(2,340)
print(e)


#TUPLES--> syntax -->() once created they cant be changed agained
a=(1,2,3,4)
print(a)
print(type(a))
print(a[1])

a=(1,2,3,4)
b=(5,6,6,7,6)
print(len(a)) #gives the number  of element of a
print(a+b) #add both the tuple
print(b*2)#merges two same tuples (we can take n numbers instead of two)
print(b.count(6))#countshow many times the elementis there  in tuple  that is passed in argument
print(b.index(6))#gives the index number of the element passed in an argument 


