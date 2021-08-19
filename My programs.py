'''
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum
print('The sum of first and second number is : ', num1, "+" , num2, "=" ,sum)
'''
'''
import calendar
y=int(input('Enter any year : '))
m=int(input('Enter any month : '))
print(calendar.month(y,m))
'''
'''
#PROBABLY MY FIRST APP
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
'''
'''
fileout=open("Student1.txt", "w")
for i in range(2):
    print(str(i)+'\n')
    name=input("Enter name of student : ")
    marks=input("Enter marks of student : ")
    fileout.write(name)
    fileout.write(marks)
    fileout.write('\n')
fileout.close()
'''
'''
myfile=open('Student1.txt', "r")
str=myfile.read()
print(str)
myfile.close()
'''
'''
myfile=open('Student1.txt', "r")
s=myfile.readlines()
print(s)
linecount=len(s)
print(linecount)
myfile.close()
'''
'''
text = 'my name is yash'
print(text.title())
'''
'''
text = 'my name is yash'
print(text.islower())
'''
'''
text = 'my name is yash'
print(text.swapcase())
'''
'''
text = "my name is yash" 
text.partition('is')
'''
'''
name=input(str("Enter your name: \n"))
print("Your name is", name, ".")
age=input("Enter you age: \n")
print("Your age is", age, ".")
'''
'''
#BUBBLE SORT
alist = list(input("Enter elements of the list : "))
print("Original list is : ", alist)
n=len(alist)
for i in range(n):
    for j in range(0, n-i-1):
        if alist[j]>alist[j+1]:
            alist[j],alist[j+1]=alist[j+1], alist[j]
            print("List after sorting: ", alist)
'''
'''
#INSERTION SORT
alist = list(input("Enter elements of the list : "))
print("Original list is : ", alist)
for i in range(1, len(alist)):
    key=alist[i]
    j=i-1
    while j>=0and key<alist[j]:
        alist[j+1]=alist[j]
        j=j-1
    else:
        alist[j+1]=key
print("List after sorting is : ", alist)
'''
'''
a='Honda'
b='Audi'
c=len(a)+len(b)
print(c)
'''
'''
perimeter=float(input("enter perimeter of square: "))
a=perimeter/4
print("The side of square is: ")
print(a)
'''
'''
#SOME MORE FUNCTION
abs(-12)
divmod(7,2)
sum([1,2,3])
max(1,2,3)
min(1,2,3)
oct(12)
hex(13)
'''
'''
#MORE BUILT-IN FUNCTION
"*".join("YASH")
"^".join(["hi", "hello"]
"hi yash".replace("yash","arpita")
'''
'''
#RANDOM() MODULE - we get any random float-point between 0.0<=N<1.0
import random
print(random.random())
'''
'''
#RANDOMINT() MODULE - returns integer N in the range (a,b), a<=N<=b
import random
print(random.randint(1,2))
'''
'''
#RANDOMUNIFORM(a,b) MODULE - returns a random floating point N such that : a<=N<=b for a<=b and b<=N<=a for b<a
import random
print(random.uniform(2,4))
'''
'''
#RANDOM RANDRANGE MODULE - returns a randomly selected element from range(start, stop, step)
import random
random.randrange(2,3,4,5)
'''
'''
#TRIANGLE STAR PROGRAM
i=0
while i<10:
    j=0
    while j<i:
        print("~", end='')
        j=j+1
    i=i+1
    print()
'''
'''
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
List = [1, 2] 
pos1, pos2  = 1, 2
print(swapPositions(List, pos1-1, pos2-1))
'''
'''
mydict={"cat":12, "dog":6, "elephant":23, "bear":20}
answer=mydict.get("cat")//mydict.get("dog")
print(answer)
'''
'''
mylist=[0,4,3,1]
mylist.remove(3)
print(mylist)
'''
'''
a=[1,2,3]
a[2]=0
a[a[2]]=5
a[1:2]=[]
'''
'''
alist=list(input("enter list: "))
print("Original List: ", alist)
alist.remove('1')
print("List after one element removed: ", alist)
'''
'''
tuple1=tuple(input("Enter tuple1: "))
tuple2=tuple(input("Enter tuple2: "))
tuple3=tuple1+tuple2
print("Tuple3 WITH ALL THE ELEMENTS OF FIRST AND SECOND TUPLES IS: ", tuple3)
'''
'''
#SORTING AN ARRAY OF INTEGER

print("Input Array Elements:")
l=list(map(int,input().split(" ")))
l.sort()
a=[0 for i in range(len(l))]
print("Input your choice:")
print("1.Arrange the Array in Ascending Order")
print("2.Arrange the Array in Descending Order")
c=int(input("Choice(1/2):"))
if(c==1):
    for i in range(len(l)):
        print(l[i],end=" ")
elif(c==2):
    for i in range(len(l)):
        a[len(l)-1-i]=l[i]
    for i in range(len(a)):
        print(a[i],end=" ")
else:
    print("Choose either 1 or 2.")

'''
#PYMARK
'''
file=open("C:\\Users\\home\\Desktop\\Student1.txt","r")
print(file.readline())
file.close()
'''
'''
file=open("C:\\Users\\home\\Desktop\\first.txt","r")
lines=file.readlines()
print(file.readline())
file.close()
file=open("C:\\Users\\home\\Desktop\\first.txt","w")
file1=open("C:\\Users\\home\\Desktop\\firstcopy.txt","w")
for line in lines:
    if 'a' in file1:
        file.write(line)
    else:
        file.write(line)
print("All line that contain a character has been removed")
print("All lines has been saved")
file.close()
file1.close()
'''
'''
file=open("C:\\Users\\home\\Desktop\\first.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+"#", end="")
        print("")
'''
'''
#FIBO CODE
def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    return fib(n-1)+fib(n-2)
n=int(input('Enter the term values:'))
if (n<0):
    print("Not defined for negative no.")
else:
    print("The required term of series of is:", fib(n))
'''
'''
#FACTORIAL OF A NUMBER
def fact(n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number:"))
if (n<0):
    print("Factorial for a negative number is not defined")
elif (n==0):
    print("Factorial for zero is 1")
else:
    print("Factorial of number:","is", fact(n))
'''



#Q1
'''
with open('Student1.txt') as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.isupper():
            count += 1
print(count)
'''
#Q2
'''
with open('Student1.txt') as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.islower():
            count += 1
print(count)
'''
#Q3
'''
stack1 = ["Yash", "Pavan", "Shubhankar"]
print("Original stack: ", stack1)
stack1.append("Om")
stack1.append("Omkar")
stack2=print("Updated stack: ", stack1)
'''
#Q4
'''
queue1 = ["Yash", "Pavan", "Shubhankar"]
queue1.append("Om")
queue1.append("Omkar")
print(queue1)
'''
#Q5
#(a)Cardinality: 4  Degree: 3
'''
import random
AR=[20,30,40,50,60,70,80,90,100];
FROM = random.randint(0,4)
TO = random.randint(2,6)
for K in range(FROM, TO+1):
    print(AR[K], end = "#")
'''
#MYSQL & PYTHON CONNECTOR
'''
import mysql.connector
mydb = mysql.connector.connect(
    host = "Prashant",
    user = "root@localhost",
    password = "yash123"
)
print(mydb)
'''
#while loop
'''
i = 1
while i < 6:
  print(i)
  i += 1
'''
'''
i = 1
while i <= 6:
  print(i)
  if i == 10:
    break
  i += 1
'''
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''
#for loop
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''
'''
for x in "banana":
  print(x)
'''
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
'''
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''
'''
for i in range(6):
    print(i)
'''
'''
i=5
while i in range (6):
    print(i)
    break # if i dont use break it continues the loop in an infinite manner
          # if i use continue it keeps going in an infinite loop
'''
'''
import math
def area():
    l = float(input("Enter length of the given triangle: "))
    b = float(input("Enter breadth of the given triangle: "))
    area = (l*b)/2
    if l < 0:
        print("Invalid input!")
    if b < 0:
        print("Invalid input!")
    else:
        print("The area of triangle is: ", area)
area()
'''
#area of user chosen shape
'''
import math
def area():
    pass
choice=int(input("Enter 1-square 2-rectangle 3- triangle: "))
if choice==1:
    side = int(input("Enter side: "))
    area1 = 4*side
    print(area1)
elif choice==2:
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area2 = length*breadth
    print(area2)
elif choice==3:
    a = int(input("enter side a : "))
    b = int(input("enter side b : "))
    c = int(input("enter side c : "))
    s = (a+b+c)/2
    print(s)
    area_of_triangle=math.sqrt(s*(s-a)* (s-b)*(s-c))
    print(area_of_triangle)
else:
    print("Invalid choice!")
area()
'''
#largest number 
'''
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
if(a>b and a>c):
    m=a
else:
    if(b>c):
        m=b
    else:
        m=c
print("Largest number among the three ",a,",",b,",",c,",","is : ", m)
'''
'''
import webbrowser
print("press 1 for war movie song :");
print("press 2 for shape of you :");
print("press 3 for ketchup song:");
print("press 4 for muqabla song:");
print("press 5 for Taekaway song:");
print("press 6 for Bymyside song:");

mychoice= input("Enter your choice : ") 
print(mychoice) 

if mychoice == "1":
                print(" You chose to play War movie song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=0kfLTq57_Y0')
elif mychoice == "2":
                print(" You chose to play shape of you song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=JGwWNGJdvx8');
elif mychoice == "3":
                print(" You chose to play ketchup song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=AMT698ArSfQ');
elif mychoice == "4":
                print(" You chose to play muqabla song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=IVMquMDUQZY');
elif mychoice == "5":
                print(" You chose to play Takeaway")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=nB2MPxZm59I');
elif mychoice == "6":
                print(" You chose to play Bymyside")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://soundcloud.com/luk3worm/luk3worm-bymyside-out-now');
else:
        print("wrong choice")

'''
#bar graph
'''
import numpy as np
import matplotlib.pyplot as plt

val = [[5.,25.,45.,20.],[4.,23.,49.,17.],[6.,22.,47.,19.,]]

X=np.arange(4)
plt.bar(X+0.00, val[0], color='b', width=0.25)
plt.bar(X+0.25, val[1], color='g', width=0.25)
plt.bar(X+0.50, val[2], color='r', width=0.25)
plt.show()
'''
'''
#PIE CHART
import numpy as np
import matplotlib.pyplot as plt

contri=[17,8.8,12.75,14]
plt.pie(contri)
plt.show()
'''
#LABELS OF PIE CHART
'''
import numpy as np
import matplotlib.pyplot as plt
contri=[17,8.8,12.75,14]
houses=['vidya', 'kshama','namrta', 'karuna']
plt.pie(contri, labels=houses)
plt.show()
'''
#MYSQL PYTHON CONNECTION
#Q1
'''
import mysql.connector
mydb = sqltor.connect(host="localhost", user="yash", password="yash@123", database="school")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
L = []
roll = int(input("Enter roll number : "))
L.append(roll)
name = input("Enter name : ")
L.append(name)
age = int(input("Enter age : "))
L.append(age)
std = input("Enter std : ")
L.append(std)
city = input("Enter city : ")
L.append(city)
student = (L)
sql="insert into student (roll,name,age,std,city) values (%s,%s,%s,%s,%s)"
mycursor.execute(sql,student)
mydb.commit()
'''
#push & pop
'''
stk=[]
ch='Y'
while(ch=='Y' or ch=='y'):
    print("Enter 1 : Push")
    print("Enter 2 : Pop")
    opt=int(input('enter ur choice:='))
    if opt==1:
        d=int(input("enter book no : "))
        stk.append(d)
    elif opt==2:
         if (stk==[]):
             print( "Stack empty")
         else:
             p=stk.pop()
             print ("Deleted element:", p)
    else:
        print('invalid choice')
        ch=(input('want to continue?'))
        if ch=="no" or "No" or "NO":
            quit
        elif ch=="yes" or "Yes" or "YES":
            continue
print(stk)
'''
#Q2
#DELETION OF RECORD(S)
'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="yash", password="yash@123", database="school")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
roll=int(input("Enter the roll number of the student to be deleted : "))
rl=(roll,)
sql="delete from Student where roll=%s"
mycursor.execute(sql,rl)
print('ATTENTION ! RECORD DELETED SUCCESSFULLY!!!')
mydb.commit()
'''
'''
ch='Y'
while (ch=='Y' or ch=='y'):
    print("Enter 1 : String palindrome")
    print("Enter 2 : prime no")
    opt=int(input('enter ur choice : '))
    if opt==1:
        str=input('Enter Text : ')
        rev=str[::-1]
        if str==rev:
            print(str, "is Palindrome")
        else:
            print(str, "is not Palindrome")
    elif opt==2:
        no=int(input('Enter Number : '))
        for i in range(2,no):
            ans=no%i
            if ans==0:
                print ("Non Prime")
                break
            elif i==no-1:
                print("Prime Number")
    else:
        print('invalid choice')
    ch=(input('want to continue?'))
'''
#Q3
'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="yash", password="yash@123", database="business")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
L=[]
code=int(input("Enter the CODE : "))
L.append(code)
iname=input("Enter the item Name: ")
L.append(iname)
qty=int(input("Enter quantity : "))
L.append(qty)
price=input("Enter price : ")
L.append(price)
company=input("Enter the company : ")
L.append(company)
st=(L)
sql="insert into ITEMS (code,iname,qty,price,company) values (%s,%s,%s,%s,%s)"
mycursor.execute(sql,st)
mydb.commit()
'''
'''
ch='Y'
while (ch=='Y' or ch=='y'):
    print("Enter 1 : count words")
    print("Enter 2 : count line")
    print("Enter 3 : count alphabets")
    print("Enter 4 : exit")
    opt=int(input('enter ur choice : '))
    if opt==1:
        f=open("student1.txt","rt")
        data = f.read()
        words = data.split()
        print('Number of words in text file :', len(words))
    elif opt==2:
        c=0
        f=open("student1.txt" , "r")
        line=f.readline( )
        while line:
            c=c+1
            line=f.readline( )
            print('no. of lines:',c)
        f.close()
    elif opt==3:
        F=open('student1.txt','r')
        data = F.read()
        number_of_alphabets = len(data)
        print('Number of alphabets in text file : ', number_of_alphabets)
    elif opt==4:
        break
        quit
    else:
        print('invalid choice')
'''
'''
import mysql.connector as sqltor
mydb = sqltor.connect(host="localhost", user="yash", password="yash@123", database="employee")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create table empdetails (emp_id varchar(4), emp_name varchar(25), gen varchar(1), phone int(10))")
'''
#To check whether the entered character is an alphabet, digit or any other character
'''
ch = input("Enter a Character : ")
if ch.isalpha():
    print("The character you entered is an alphabet.")
elif ch.isdigit():
    print("The character you entered is a digit.")
else:
    print("You entered character is some other character.")
'''
#PALINDROME
'''
str=input('Enter Text : ')
rev=str[::-1]
if str==rev:
    print(str, "is a Palindrome")
else:
    print(str, "is not a Palindrome")
'''
#CREATING TABLE FORM PYTHON TO MYSQL
'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="yash", password="yash@123", database="college")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create table students (stud_id varchar(4), name varchar(25), class varchar(4), gen varchar(1), city varchar(20))")
'''
#INSERTING VALUES INTO TABLE CREATED
'''
import mysql.connector as sqltor
mydb = sqltor.connect(host="localhost", user="yash", password="yash@123", database="college")
if mydb.is_connected():
    print('Successfully connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
L=[]
stud_id = input("Enter student ID : ")
L.append(stud_id)
name = input("Enter the student Name : ")
L.append(name)
clas = input("Enter class : ")
L.append(clas)
gen = input("Enter gender : ")
L.append(gen)
city = input("Enter the city : ")
L.append(city)
st=(L)
sql="insert into students (stud_id, name, class, gen, city) values (%s,%s,%s,%s,%s)"
mycursor.execute(sql,st)
mydb.commit()
'''
# Python 3 program for recursive binary search.
'''
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [2,3,6,12,10,34,40]
x = 10
# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
'''
'''
import mysql.connector as sqltor
mydb = sqltor.connect(host="localhost", user="yash", password="yash@123", database="college")
if mydb.is_connected():
    print('Successflly connected to MySQL Database')
else:
    print('Failed to connect to MySQL Database')
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("select gen from students")
'''
#DATE & TIME
'''
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (str(now))
'''
#PROFIT/LOSS
'''
actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))
 
if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
'''

'''
import webbrowser
print("press 1 for war movie song :");
print("press 2 for shape of you :");
print("press 3 for ketchup song:");
print("press 4 for muqabla song:");
print("press 5 for Taekaway song:");
print("press 6 for Bymyside song:");

mychoice= input("Enter your choice : ") 
print(mychoice) 

if mychoice == "1":
                print(" You chose to play War movie song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=0kfLTq57_Y0')
elif mychoice == "2":
                print(" You chose to play shape of you song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=JGwWNGJdvx8');
elif mychoice == "3":
                print(" You chose to play ketchup song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=AMT698ArSfQ');
elif mychoice == "4":
                print(" You chose to play muqabla song")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=IVMquMDUQZY');
elif mychoice == "5":
                print(" You chose to play Takeaway")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://www.youtube.com/watch?v=nB2MPxZm59I');
elif mychoice == "6":
                print(" You chose to play Bymyside")
                webbrowser.get("C:/Program Files (x86)/google/Chrome/Application/chrome.exe %s").open('https://soundcloud.com/luk3worm/luk3worm-bymyside-out-now');
else:
        print("invalid choice!")
'''

#bar graph
'''
import numpy as np
import matplotlib.pyplot as plt

val = [[5.,25.,45.,20.],[4.,23.,49.,17.],[6.,22.,47.,19.,]]

X=np.arange(4)
plt.bar(X+0.00, val[0], color='b', width=0.25)
plt.bar(X+0.25, val[1], color='g', width=0.25)
plt.bar(X+0.50, val[2], color='r', width=0.25)
plt.show()
'''
#PIE CHART
'''
import numpy as np
import matplotlib.pyplot as plt

contri=[17,8.8,12.75,14]
plt.pie(contri)
plt.show()
'''
#LABELS OF PIE CHART
'''
import numpy as np
import matplotlib.pyplot as plt

contri=[17,8.8,12.75,14]
houses=['vidya', 'kshama','namrta', 'karuna']
plt.pie(contri, labels=houses)
plt.show()
'''
#TABLE OF ANY NUMBER
'''
num = int(input("Enter number of which table you want : "))
table = int(input("Enter range till when the table of entered number will be created : "))
for i in range(1,table):
    print(i*num)
'''
#FUNCTION ARGUMENTS
'''
def defaultarg(a,b,c):
    print("a = {}, b = {}, c = {}, ...".format(a,b,c))
defaultarg(10,20,30)
'''
'''
for i in range(1,20):
    if (i%2):
        continue
    print(i)
'''
#GENERATORS
'''
def my_generator():
    n=1
    print("This gets printed first.")
    yield n

    n+=1
    print("This gets printed second.")
    yield n

    n+=1
    print("This gets printed third.")
    yield n

a = my_generator()
next(a)
next(a)
next(a)

print("Using for loop.")
for item in my_generator():
    print(item)
'''
#REVERSING STRING METHOD 2
'''
def rev_string(my_string):
    length = len(my_string)
    for i in range(length -1, -1, -1):
        yield my_string[i]
for char in rev_string("PYTHON"):
    print(char)
'''
#PROGRAM FOR COUNTDOWN
'''
i = int(input("Enter a number : "))
while i > 0:
    print(i)
    i -= 1
'''
'''
i = 30
while i in range(30,50):
    print(i)
    i += 1
else:
    print("Displayed Successfully!")
'''
#TWO SYMBOL PATTERN PROGRAM
'''
n = int(input("Enter number of layers you want in the pattern : "))
i = 1
while i <= n:
    j=1
    while j<=n-1:
        print("()", end="")
        j=j+1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j=j+1
    print()
    i=i+1
'''
#NESTED IF
'''
num = float(input("Enter a number : "))
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Entered number is a positive number.")
else:
    print("Entered number is a negative number.")
'''
#REGULAR EXPRESSION
'''
import re
animalstr = "cat rat mat fat pat"
allanimals = re.findall("[crmfp]at", animalstr)
for i in allanimals:
    print(i)
print()
'''
'''
import re
owlfood = "rat cat mat pat"
regex=re.compile("[cr]at")
owlfood=regex.sub("owl", owlfood)
print(owlfood)
'''
#ADDING ELEMENTS TO LIST
'''
a_letter = []
b = str(input("Enter a word : "))

for letter in b:
    a_letter.append(letter)
print("Elements of the word you entered have been successfully added to this list :", a_letter)
'''
'''
num_list = [x for x in range(10) if x%2==0]
print(num_list)
'''
#MATRIX TRANSPOSE PROGRAM
'''
matrix = [[1,2], [3,4], [5,6]]
transpose = [[row[i] for row in matrix]for i in range(2)]
print(transpose)
'''
#FACTORIAL USING RECURSION
'''
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
n = int(input("Enter any number : "))
print("Factorial of ",n," is : ", fact(n))
'''
#SHALLOW AND DEEP COPY SEGMENT
#ID
'''
list1=[[1,2],[3,4],[5,6]]
list2 = list1
print("list1 -> ",list1)
print("list2 -> ",list2)
print("id of list1 -> ", id(list1))
print("id of list2 -> ", id(list2))
list1.append([10, 11])
print("list1 -> ", list1)
print("list2 -> ", list2)
'''
#CREATING COPY USING SHALLOW COPY
'''
import copy

old_list = [[1,2],[3,4]]
new_list = copy.copy(old_list)
print("Old list -> ", old_list)
print("New list -> ", new_list)

old_list[1][1]='aa'

print("Old list -> ", old_list)
print("New list -> ", new_list)
'''
'''
import copy

old_list = [[1,2],[3,4]]
new_list = copy.deepcopy(old_list)
print("Old list -> ", old_list)
print("New list -> ", new_list)
'''
#LAMBDA FUNCTION
'''
a = lambda x:x*2
print("Double of 10 is : ", a(10))
'''
#ASSERT
#if true code runs, if false then code stops and give Assertion error
'''
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
'''
