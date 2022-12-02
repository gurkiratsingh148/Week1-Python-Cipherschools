print("Hello world")
print("hello'world'world")
print('hello "world" world')
print('liine A\nline B') #\n is for new line
print('Name\tGurkirat')
print('this is backslash\\')
print('hell\blo')
#this is a comment
#output: line A\n Line B
print('line A \\n line B')
print("\\\" \\\'")
print(r"line A \n line B")
#emoji
print("\U0001F602")
print("\U0001F603")
# Python as clculator
print(2+3*4)
print(2/4)
print(4/2)
print(4//2)
print(2//4)
print(2**3)
print(2**0.5)
print(round(2**0.5,4))

# variables 
mun1=2
print(mun1)
name='Gurkirat'
print(name)

# conventions
user_one_name='Rajnesh' #snake case writing
userOneNmae='Mohit' #camel case writing

#string concatenation
first_name='Gurkirat '
last_name='Singh '
full_name=first_name+last_name
print(full_name)
print(full_name*3)

#user input
name=input("type your name ")
age=input("what is your age ")
print("your age is "+age)

#int function
num1=int(input())
num2=int(input())
total=num1+num2
print(total)

num1=str(4)
num2=float("44")
num3=int("33")
print(num2+num3) #float

name,age="Gurkirat","18"
print("Hello "+name+" your age is " +age)

#two or more input in one line
name,age=input("enter your name and age :").split()
print(name)
print(age)

#string formatting
name="Gurkirat"
age=18
print("Hello {} your age is {}".format(name,age))
print((f"Hello {name} your age is {age}"))

#string indexing
a="python"
print(a[2])
print(a[4])
print(a[-1])

#slicing of string
a="python"
print(a[0:3])

#step argument 

print("Gurkirat"[1:4])
print("Gurkirat"[0:3:2])
print("Gurkirat"[0::2])

#string methods
name="GuRkIraT sInGh"
#length of string
print(len(name))
#lower case
print(name.lower())
#upper case
print(name.upper())
#title method
print(name.title())
#count methos
print(name.count("Y"))

#Strip method
name="   Gurkirat    "
dot=".."
#lstrip() method
print(name+dot)
print(name.lstrip()+dot)
print(name.rstrip()+dot)
print(name.strip()+dot)

name="   Gurkir  at"
print(name.replace(" ","")+dot)

#replace and find
string="he is a good batsman and is wicket keeper"
print(string.replace(" ","_"))
i=(string.find("is"))
j=(string.find("is",i+1))
print(j)

#center method
name="gurkirat"
print(name.center(10,"*"))

name=input("Enter your mane:")
print(name.center(len(name)+6,"^"))

# use of if
age=int(input("enter your age "))
if age>=14:
    print("you are above 14")

#pass statement
x=18
if x>18:
    pass

#else statement
age=int(input("enter your age "))
if age>=18:
    print("you can play")
else:
    print("sorry you can not play")


# and ,or operators
name='abc'
age=19
if name=='abc' and age==19:
    print("True")
else:
    print('False')

if name=='abc' or age==23: 
    print("True")
else:
    print('False')

# if-elif-else
age=int(input("enter your age: "))
if 0<age<=3:
    print("Ticket price: Free")
elif 3<age<=10:
    print("Ticket price: 150")
elif 11<=age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")

# in keyword

name="Harshit"
if 'a' in name:
    print("a is in name")
else:
    print("a is not in name")

#check empty
name=input("enter your name: ")
if name:
    print("string is not empty")
else:
    print("string is empty")


#while loop
# print("hello world")
i=1
while i<=10:
    print(f"hello world {i}")
    i+=1


#sum of numbers
total=0
i=1
while i<=10:
    total=total+i
    i+=1
print(total)

#infinite loop

while True:
    print("hello world")

#for loop

for i in range(10):
    print("hello world")