print("Hello World")

# -----------------------------

print (25)

# -----------------------------

print(25)
#Print(25) # capital P will be treated as different word
#print(025) #leading zeros in decimal integer literals are not permitted
print(0.12) #allowed to write

# -----------------------------

print            
(25)

# -----------------------------

NAME = 'Tejal'
AGE = 20
PRICE = 15000
print(NAME)

print(AGE,PRICE)

print ("My name is",NAME,"and My age is",AGE)

# -----------------------------

print(type('25'))

# -----------------------------

## Area of square

a=int(input('give side of a:'))
area = 4 * a
print(area)


# -----------------------------

## Area of circle

r=int(input('Radius of circle:'))
pi = 3.1456
area_of_circle = 2 * pi * r * r
print("area_of_circle" ,area_of_circle)


# -----------------------------

print(type(True)) 

# -----------------------------

A = None
print (type(A))
print(A)


# -----------------------------

A=10
print(A)
print(type(A))

# -----------------------------

x = lambda : x* x
print(x)

# -----------------------------

11/2

# -----------------------------

print(not True)
print (not False)

a =50
b=40
print(not(a > b))
print(a>b or b>a)

# -----------------------------

a=2
b=4.25
sum = a+b
print(sum)

# -----------------------------

a="2"
b="4"
sum = a + b
print(sum)

# -----------------------------

# conversion of string to int
a= 25
b="56"
c=int(b)
print(a+c)

# -----------------------------

#conversion of float to int
a=20.5
b=20
c=int(a)
print(b+c)


# -----------------------------

# write a program to input 2 numbers and print their sum

num1 = int(input("Enter the First Num:"))
num2 = int(input("Enter the Second Num:"))

sum = num1 + num2
print("Addition of",num1,"and",num2 ,"is:",sum)

# -----------------------------

# Wap to input side of square and print its area

a=int(input('Give side of a:'))
area = 4 * a
print(area)


# -----------------------------

# WAP to input 2 floating point numbers and print their average
A = float(input("Enter the First Num:"))
B = float(input("Enter the Second Num:"))
Avg = (A+B) /2
print("The Average is",Avg)

# -----------------------------

# Print true if a greater than or equal to b if not print false
P = 25
Q = 75
if Q > P or Q == P :
    print(True)
else:
    print(False)

# -----------------------------

str1 = "Tejal"
str2 = "Pagar"
print(str1,str2)


# -----------------------------

str1 = "Tejal"
str2 = "Pagar"
str = str1 +"   "+str2
print(str)

# -----------------------------

#Indexing
b="b"
str = "apna_college"
print(str[0],str[3])
print(str[1:])
str[0] == b

# -----------------------------

s="madam is good"
print (s[::-1])

# -----------------------------

str ="i am A coder"
print(str.count("a"))
print(str.endswith("er"))
print(str.capitalize())
print(str.find("A"))
str.capitalize ##will only show will not change
print(str)
str1 = str.replace("A","a")
print(str1)
print(str1.count("a"))

# -----------------------------

## Practice Questions

# WAP to input user's First name and return its length
name=input("Enter Your first Name:")
print("Hello",name)
print("Length of Your name is",len(name))

#WAP to find the occurrenceof '$' in a string
str="Hie $ this is $ $ymbol,How have you $ been Doing"
print(str.count("$"))

# -----------------------------

light ="pink"
if light== "red":
    print("STOP")
elif light == "Yellow":
    print("LOOK")
else:
    print("Light is broken")

# -----------------------------

#grade sttudents based on marks
marks =102
if marks >= 90 :
    if marks > 100:
        print("Enter Valid Marks")
    else:
        print("A")
elif 90> marks and marks>=80:
    print("B")
elif 80>marks and marks>=70:
    pprint("c")
elif 70>marks :
    print("D")
else:
    print("FAIL")


# -----------------------------


## Practice Questions

# WAP to check if a number is entered by user is odd or even

num=int(input("Enter the number:"))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# -----------------------------


# Wap to find the greatest of 3 num entered by user
a =10
b =51
c=15

if a>b and a>c:
    print("A is the greatest number")
elif b>c :
    print("B is the greatest number")
else:
    print("C is the greatest number")


# -----------------------------

# WAP to check if a number is multiple of 7

num=int(input("Enter the number:"))
if num % 7 == 0:
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7") 
 

# -----------------------------

marks=[10,20,30,40,50]
print(len(marks))
print(marks)
marks[0]=11
print(marks)

# -----------------------------

L =list([1,2,3,4,5])
print(L)

# -----------------------------

marks=[10,20,30,40,50]
print(marks[1:5])
print(marks[0:])
print(marks[-3:-1])
print(marks[::-1])

# -----------------------------

mark=[22,56,78,10,6,27]
mark.append(5)
print(mark)
mark.sort()
print(mark)
mark.insert(4,45)
mark.reverse()
print(mark)

# -----------------------------

tup=(2,1,2,3)
tup1=(1,) # if this not applied then it will be int type
tup.index(2)
tup.count(2)
# tup3=(1)
# type(tup3)

# -----------------------------

tup=("C","D","A","A","B","B","A")
tup1 = tuple(sorted(tup)) 
print(tup1)

# -----------------------------

# WAP to ask the user to enter the names of their thrree favoritemovies and store them in a list
Movie=[]
a=input("Enter your first Favorite movie name")
b=input("Enter your second Favorite movie name")
c=input("Enter your third Favorite movie name")
Movie.append(a)
Movie.append(b)
Movie.append(c)
print(Movie)

# -----------------------------

# WAP to check if a list contains a palindrome of elements 
Num=[1,2,3,2,1]

A=Num.copy()
A.reverse()

if (A == Num):
    print("The list is Palindrome")
else:
    print("ok")


# -----------------------------

# WAP to count the number of students with the "A" grade in the following tuple
tup=("C","D","A","A","B","B","A")
tup.count("A")  
#tuples cannot be sorted directly coz tuple is immutable
#to sort tuuple first convert it into list then reverse the list

# -----------------------------

# store the above values in a list and sort the m from "A" to "D"
list =["C","D","A","A","B","B","A"]
list.sort()
print(list)


# -----------------------------

A = list(range (0,6,2))
print(A)

# -----------------------------

for i in range(0,6):
    print(i)

# -----------------------------

for i in range (10,0,-1):
    print(i)
#for i in range (10,10,-1):     #doesn't give any output
    print(i)
    

# -----------------------------

for i in range (10,10,-1):
    print(i)
#same start and end does not givee any answer

# -----------------------------

for i in range(0, 6):
    for j in range(0, i+1):
        print(j, end=" ")
    print()


# -----------------------------

for i in range(0, 6):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

# -----------------------------

dict={
    "name":"Tejal",
    "age":19,
    "Marks":[98,97,85],
    10:"start"
}

print(dict)

# -----------------------------

print(dict.keys())
print(dict.values())
print(dict.items()) #returns all key value pairs in tuple 
dict.get("name")
dict.update({"pn":7887})
print(dict.items())

# -----------------------------

collection={1,2,3,4}
print(collection)
print(type(collection))

# -----------------------------

# empty set
collection=set()
type(collection)
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(1)
print(collection)
collection.remove(1)
print(collection)

# -----------------------------

num2={1,3,2,5,6,3,2,9}
num1={1,2,3,4,5,6}
num3= num2.union(num1)
num4=num2.intersection(num1)
print(num3)
print(num4)

# -----------------------------

# store following word meanings in python dictionary

Dict={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(Dict)

# -----------------------------

# you are given a list of subjects for students.
#assume one classroom is required for 1 subject.
#how many classroms are needed by all students.
set1={"python","java","C++","python","Javascript","java","python","java","C++","C"}
print(len(set1))

# -----------------------------

# WAP to enter marks of three subjects from the user and store them in a dictionary.
#start with an empty dictionary and add one by one.
#use subject name as keynand marks as values.
A=int(input("Enter marks of first subject:"))
B=int(input("Enter marks of second subject:"))
C=int(input("Enter marks of third subject:"))
dict={}
dict.update({"A":A})
dict.update({"B":B})
dict.update({"C":C})
print(dict)

# -----------------------------

# figure out a way to store 9,9.0 as separate values in set

collection=set()
collection.add(int(9))
collection.add(str(9.0))
print(collection)

# -----------------------------

