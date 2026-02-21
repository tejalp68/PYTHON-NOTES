count = 0
while count <= 5:
    print("Hello")
    count += 1

# -----------------------------

## Practice questions

# -----------------------------

#print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# -----------------------------

#print the following ele of the following list using loop:
#   [1,4,9,16,25,36,49,64,81,100]
count = 1
while count <= 10:
    print(count ** 2)
    count = count + 1

# -----------------------------

#print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# -----------------------------

# print the multiplication table of n number
i = 0
while i<=30:
    print(i)
    i = i+3   #using my logic

# -----------------------------


A=int(input("Enter the Number"))
i=1
while i<=10:
    print(A*i)
    i +=1

# -----------------------------

#print the following ele of the following list using loop:
#   [1,4,9,16,25,36,49,64,81,100]

num=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx <=len(num)-1:
    print(num[idx])
    idx +=1


# -----------------------------

#search for number x in this tuple using loop

# # STEP-1 Converting tuple into list
# tup1 = (1,4,9,16,25,36,49,64,81,100)
# list1 =list(tup1)

# STEP-2 using while loop
tup1 = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter the Number"))
idx = 0
while idx < len(tup1):
    if (tup1[idx] == num):
        print("Found",num,"at index",idx)
        break;
    else:
        print("Finding...")
    
    idx += 1
    


# -----------------------------

##use of Break
i=0
while i<=10:
    print(i)
    if (i==3):
        break;
    i +=1    

# -----------------------------

##use of continue
i=0
while i<=5:
    if (i == 4):
        i+=1
        continue;#Acts as skip
    print(i)
    i  +=1

# -----------------------------

## use continue to print odd values and skip even values
i=0
while i <= 10:
    if (i % 2 == 0 ):
        i += 1
        continue;
    print(i)
    i +=1

# -----------------------------

## use continue to print even values and skip odd values
i=0
while i <= 10:
    if (i % 2 != 0 ):
        i += 1
        continue;
    print(i)
    i +=1

# -----------------------------

## we cant get the even and odd values using break because it breaks the loop
i=0
while i <= 10:
    print(i)
    if (i % 2 == 0 ):
        break;
    i +=1

# -----------------------------

list1 =[1,2,3]
for i in list1:
    print(i)

# -----------------------------

##PRACTICE QUESTIONS

# print the elements of the following list using loop
num=[1,4,9,16,25,36,49,64,81,100]

for i in num:
    print(i)

# -----------------------------

#search for number x in this tuple using loop
# tup1 = (1,4,9,16,25,36,49,64,81,100)

tup1 = (1,4,9,16,25,36,49,64,81,100)
idx =0
x= int(input("Enter num"))
for i in tup1:
    if (i == x):
        print(x,"is Found at",idx)
    idx += 1    
else:
    print("Number not Found")

# -----------------------------

# WAP to find the sum of first n numbers
# using while
n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 1

print("Sum of first", n, "numbers is:", sum)



# -----------------------------

# WAP to find the factorial of first n numbers
# using for
n = int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact =fact *i
    print(fact)

# -----------------------------

## fact of 0-9 
fact = 1
for i in range(1,n+1):
    fact =fact *i
    print(fact)

# -----------------------------

def sum(a,b):
    sum=a+b
    return sum
  
print(sum(2,3))

# -----------------------------

# a function that returns multiple values
def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)
print(x, y, z)


# -----------------------------

# average of three numbers
def avg_fun(a,b,c):
    add=a+b+c
    avg= add // 3
    return avg
avg = avg_fun(3,4,5)
print(avg)

# -----------------------------

## to print multiple values on same line

print("Tejal" ,end=" <3 ")
print("Pagar")
print(#hie this 
"Run")

# -----------------------------

print("Hello # this is comment")
print("Hello")      # This is a comment (not printed)
print("Hello # hi") # This is part of the string (printed)



# -----------------------------

##Practice questions 

# -----------------------------

# WAP to print the element of a list in a single line 
lst =["RAM","SHAM","RADHA","RANI"]
def prt(list):
    for i in lst:
        print(i ,end=" ")
prt(lst)

# -----------------------------

# WAP ro find the factorial of n
n=int(input("Enter the number"))
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact =fact * i
    print(fact)    
calc_fact(n)

# -----------------------------

# WAP to print the length of a list
lst =["RAM","SHAM","RADHA","RANI"]
def return_len(list):
    return len(list)

return_len(lst)

# -----------------------------

# WAP to convert USD to INR
a=int(input("Enter the amount you want to convert from USD to INR :"))
def USD_to_INR(a):
    calc = a * 90.03
    return calc
    
USD_to_INR(a)

# -----------------------------

# to write even and odd string acc to num

def classify(n):
    for i in range(1,n+1):
        if (i % 2 == 0):
            print(i,"Even")
        else:
            print(i,"Odd")
            
classify(10)            

# -----------------------------

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# -----------------------------

#factorial
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
fact(5)

# -----------------------------

## Practice questions
# write a reursive function to calculate the sum of first n natural numbers

def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
sum(10)      

# -----------------------------

# write a recursive function to print all elements in a list .hint use list and index as parameters
lst = [1,2,3,4,5,8,4,5,7,9]

def func(list ,i=0):
    if (i >= len(list)):
        return       
    print("Element of list",list[i],"has index",i)
    
    func(list,i+1)
    
func(lst)


# -----------------------------

f = open("demo.txt" ,"r")
data=f.read()
print(data)
print(type(data))

# -----------------------------

f = open("demo.txt" ,"r")
# data =f.read()
# print(data)
# f1=f.read(10)
data1 =f.readline()
print(data1)
data2 =f.readline()
print(data2)
data3 =f.readline()
print(data3)

# -----------------------------

f = open("demo.txt" ,"w")
f.write("I want to learn Python")

# -----------------------------

f = open("demo.txt" ,"a")
f.write("\nthis is new line")

# -----------------------------

f = open("demo.txt","r")
data = f.read()
print(data)

# -----------------------------

import os
os.remove("demo.txt")

# -----------------------------

## practice Questions

# -----------------------------

# Create a new file "Practice.txt" using python.Add the following data in it:
# Hi everyone
# We are learning file I/O
# Using Python
# I like Programming in Python 
f = open("Practice.txt","w")
f.write("Hi everyone \nWe are learning file I/O \nUsing Python \nI like Programming in Python" )

# -----------------------------

f=open("Practice.txt")
df=f.read()
print(df)
# f.close()

# -----------------------------

#WAF that replace all occurrences of python with "java" in above file
f=open("Practice.txt","r+")
df=f.read()
dd=df.replace("Python","Java")
print(dd)

# -----------------------------

# Search if the word "learning" exists in the file or not
f=open("Practice.txt","r+")
df=f.read()
if(df.find("learning") != -1):
    print("Exists")
else:
    print("not exists")



# -----------------------------

#waf to find  in which line of the file does the word learning occur first print -1 if word does not found
with open("Practice.txt","r+") as f:
    df=f.read() 
    if(df.find("learning") != -1):
        print("Exists")
    else:
        print(-1)


# -----------------------------

#from a file containing numbers separated by  comma ,print the count of even numbers
with open("new.txt","w") as f:
    f.write("1,22,33,24,15,86,7,78,19,10")
    
    

# -----------------------------

with open("new.txt","r") as f:
    data =f.read()
    print(data)
    num=""
    for i in range(len(data)):
        if (data[i] ==","):
            print(int(num))
            num=""
        else:
            num += data[i]

# -----------------------------

count=0
with open("new.txt","r") as f:
    data =f.read()
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 ==0):
            print(val)
            count +=1
print(count)    

# -----------------------------

total = 0

with open("new.txt", "r") as f:
    data = f.read()
    nums = data.split(",")

    i = 0
    while i < len(nums):
        if int(nums[i]) % 2 == 0:
            total = total + int(nums[i])
        i += 1

print(total)

# -----------------------------

class Student():
    name= "Karan Kumar"
s1 = Student()
print(s1.name)

# -----------------------------

class Car():
    color = "Blue"
    Brand ="Mercedes"
s = Car()
print(s.color,s.Brand)

# -----------------------------

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks =marks

    def hello(self):
        print("Hello",self.name,"Welcome to our Company")
    def get_marks(self):
        return self.marks
    def get_name(self):
        re

s1 = Student("Kushal",97)
print(s1.name,s1.marks)
s1.hello()
s1.get_marks()

# -----------------------------

# practice  Questions


# -----------------------------

# Create student class that takes name and marks of 3 subjects as arguments in constructorr
#then create a method to print the average
class Student():
    def __init__(self,Name,Phy,Chem,Math):
        self.Phy=Phy
        self.Chem=Chem
        self.Math=Math
    def calc_avg(self):
        avg =self.Phy+self.Chem+self.Math
        Avg =avg / 3
        print("Average of Subject is",Avg)
        
s1 = Student("Tejal",99,97,98)
s1.calc_avg()

# -----------------------------

#Create Account class with 2 attributtes -balance and account no.
# Create methods for debit ,credit and printing the balance.

class Account():
    def __init__(self,name,accNumber,balance):
        self.name= name
        self.accNumber = accNumber
        self.balance=balance
     
    def credit(self):
        self.amount =int(input("Enter Amount you want to Credit"))
        print(self.amount,"Amount is credited")
        self.balance = self.balance + self.amount
        print("Amount After crediting",self.balance)    
        
    def debit(self):
        self.am =int(input("Enter Amount you want to Debit"))
        print(self.am,"Amount is debited")        
        self.balance = self.balance - self.am
        print("Amount After debiting",self.balance)
        
    def print_balance(self):
        print(self.balance)
        

        
A =Account("Ram",101,10200)
A.print_balance()

A.credit()
A.debit()


# -----------------------------

## del keyword 
del A.name
print(name)

# -----------------------------

## Private attributes

class Account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
a = Account(101,"oplk")
print(a.acc_no)
print(a.acc_pass)

# -----------------------------

class Car():
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("car stopped")
        
class Toyota(Car):
    def brand(self,brand):
        self.brand = brand
        print("Car brand is",self.brand)
        
class Fortuner(Toyota):
    def __init__(self ,type):
        self.type= type
        
# car1 = Toyota("Fortuner")    
car2 = Fortuner("diesel")
car2.start()
car2.brand("ford")

# -----------------------------

## SUPER KEYWORD

class Car():
    def __init__(self,type):
        self.type =type
        
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("car stopped")
        
class Toyota(Car):
    def __init__(self,brand,type):
        self.brand = brand
        print("Car brand is",self.brand)
        super().__init__(type)

c1= Toyota("fortuner","diesel")
        
print(c1.type)

# -----------------------------

for i in range(0 ,15):
    for j in range(1 ,i+1):
        print("*",end=" ")
    print()
for i in range(15 ,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

# -----------------------------

# Upper half (increasing)
for i in range(1, 16):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower half (decreasing)
for i in range(14, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# -----------------------------

n = 5

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)



# -----------------------------

## Property Method

# -----------------------------

class Student():
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy = phy
        self.chem = chem
    @property
    def percentage(self):
        return str((self.math+self.phy+self.chem)//3) + "%"

s1 = Student(98,95,86)
print(s1.percentage)
s1.phy = 91
print(s1.percentage)

# -----------------------------

## use of dunder function and operator overloading

# -----------------------------

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real ,"i +",self.img ,"j")

    def add(self ,num2):                    ## without using dunder func
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
num1 = Complex(3,4)
num1.show()
num2 = Complex(4,2)
num2.show()

num3 = num1.add(num2)
# num3=num1+num2
num3.show()

# -----------------------------

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real ,"i +",self.img ,"j")

    def __add__(self ,num2):                    ## with using dunder func
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
  
    def __sub__(self ,num2):                    ## with using dunder func
        newReal = self.real - num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
num1 = Complex(3,4)
num1.show()
num2 = Complex(4,2)
num2.show()

num3 = num1 + num2
num3.show()

num4 = num1 - num2
num4.show()

# -----------------------------

## Practice Questions

# -----------------------------

# Define a circle class to create a circle with radius r using the constructor
# Define an Area method of the class which calculates the area of circle
# Define a perimeter method of class which allows you to calculate the perimeter of the circle

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area =int( 3.14 *self.radius * self.radius)
        print("Area of circle is",area)
    def perimeter(self):
        perimeter = int(2 * 3.14 *self.radius)
        print("Perimeter of circle is",perimeter)

num1 = Circle(5)
num1.area()
num1.perimeter()

# -----------------------------

class Employee():
    def show(role,department,salary):
        print("Role of Employee is",role)
        print("Department of Employee is",department)
        print("Salary of Employee is",salary)
Employee.show("ramf","dfsf",4652)

# -----------------------------

# Define a Class Employee with att role,salary & department
# this class also has show methods
# create an engineer class that inherits properties of Employee & has additional att name & age

class Employee():
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    def show(self):
        print("Role of Employee is",self.role)
        print("Department of Employee is",self.department)
        print("Salary of Employee is",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        self.name = name
        self.age = age
        super().__init__(role,department,salary)

    def showStud(self):
        print("Name of Employee is",self.name)
        print("Age of Employee is",self.age)
        

std =Engineer("Rahul Kumar",22,"DATA Engineer" ,"DATA Handling", 150000)
std.showStud()
std.show()

# -----------------------------

## create a class called order which stores items and its price
# use dunder function __gt__() to convey that:
#     order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self ,other):
        if (self.price > other.price):
            print(self.item ,">",other.item )

order1 = Order("Laptop", 55000)
order2 = Order("Mobile", 30000)
od3 = order1 > order2
# print(od3)


# -----------------------------

# Define a Class Employee with att role,salary & department
# this class also has show methods
# create an engineer class that inherits properties of Employee & has additional att name & age
