# %%
#Arthimetic operators
a=10
b=3

print("Addition:" ,a+b)
print("Subraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor division:", a//b)
print("remainder:", a%b)
print("Power:", a**b)

# %%
#bitwise operators
a=11
b=5

print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)


a=8
b=13
print(a&b)
print(a|b)
print(a^b)


# %%
#simple calculator

a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("Addition:" ,a+b)
print("Subraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)


# %%
#student marks calculator
name = input("enter your name:")

m1 = int(input("enter python marks:"))
m2 = int(input("enter java marks :"))
m3 =int(input("enter sql marks:"))

total =m1+m2+m3
average=total/3

print("/n---- students report-----")
print(  "Name:", name)
print("python marks:", m1)
print("java marks:", m2)
print("sql marks:", m3)
print("total marks:", total)
print("average marks:", average)


# %%

#shopping bill calculator
price1 = float(input("enter produt 1 price:"))
price2 = float(input("enter product 2 price:"))
price3 = float(input("enter product 3 price:"))

total = price1+price2+price3

discount =total*0.10
final_amount  =  total-discount


print("discount:", discount)
print("final amount:", final_amount)
print("total bill:", total)


# %%
#bank balance
balance=10000

deposit=5000
balance += deposit

print("after deposit balance:", balance)
withdraw=2000
balance -= withdraw
print("after withdrawal balance:", balance)


# %%
#login validation
username = input("enter username:")
password = input("enter password:")

if username == "admin" and password == "password":
    print("login successful!")
else:
    print("invalid credentials!")


# %%
#identity operators
a=None

print(a is None)
print(a is not None)


#bitwise operators
a=5
b=3

print(a&b) #bitwise AND
print(a|b) #bitwise OR
print(a^b) #bitwise XOR

# %%
numbers=[10,40,50,]
numbers.clear()
print(numbers)

numbers=[10,20,30,40]

print(numbers.index(30))

# %%
#Electricity bill calculator
units = int(input("Enter the number of units consumed: "))

rate=6

bill=units*rate


print("Electricity bill:", bill)

# %%
#travel expense calculator
travel = float(input(" travel expense: "))
food = float(input("food expense: "))
hotel = float(input("hotel expense: "))

total_expense = travel + food + hotel

# %%
#list python
#list is an ordered and changeble collection  that can store multiple values.
marks=[80,90,75,85]
       
print(marks)

#accessing list elements
marks=[80,90,75,85]

print(marks[0]) #accessing first element
print(marks[1]) #accessing second element   
print(marks[2]) #accessing third element       

#change  elements in a list
marks=[80,90,75,85]
marks[1]=95

print(marks)


#remove elements from a list
marks=[80,90,75]

marks.remove(75)

# %%
#list
numbers=[40,10,30,20]
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort()

# %%
#list

numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

# %%
#temparature check
temparature = float(input("enter temparature"))

if temparature >40:
    print("High temparature")


# %%
number = int(input("enter a number:"))

if number %5== 0:
    print("divisible by 5")

# %%
marks = int(input("Enter marks:"))

if marks >= 40:
    print("pass")
else:
    print("fail")

# %%
number = int(input("Enter a number:"))

if number >=0:
    print("positive")    
else:
    print("negative")

# %%
marks = int(input("enter marks:"))
if marks >=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("Grade C")
elif marks >=40:
    print("Grade D")
else:
    print("fail")

# %%
a = int(input("Enter  first number"))
b = int(input("Enter second number"))

if a>b:
    print("Largest:",a)
elif b>a: 
    print("Largest:",b)
else:  
    print("Both are equal")

# %%
a = int(input("Enter  first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if a>=b and a >=c:
    print("Largest:",a)
elif b>=a and b>=c: 
    print("Largest:",b)
else:  
    print("Largest:",c)

# %%
day = int(input("Enter a number"))
if day==1:
    print("monday")
if day==2:
    print("tuesday")
if day==3:
    print("wednesday")
if day==4:
    print("thursday")
if day==5:
    print("friday")
if day==6:
    print("saturday")
if day==7:
    print("sunday")


# %%

a = float(input("Enter first number"))
b = float(input("Enter second number"))
operator = input("Enter operator(+,-,*,/)")

if operator=="+":
    print("result:",a+b)
elif operator =="-":
    print("result:",a-b)
elif operator=="*":
    print("result:",a*b)
elif operator=="/":
    if b !=0:
        print("result:",a/b)
    else :
        print("cannot divide by zero")
else :
    print("invalid operator")


# %%
username = input("Enter username:")
password =input("Enter password:")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
     print("Wrong username")   


# %%
balance = float(input("Enter balance:"))
amount = float(input("Enter withdrawal amount:"))

if amount >0:
    if amount<=balance:
        balance=balance-amount
        print("Withdrawal successful")
        print("Remaining balance:",balance)  
    else:
        print("Insufficient balance")
else:  
    print("Invalid amount")


# %%
marks = int(input("Enter marks:"))
attendence = float(input("Enter attendence percentage"))

if marks >= 40:
    if attendence >=75:
        print("Eligible")
    else:
        print("Not eligible due to attendence")
else:
    print("Fail")


# %%
age = int(input("Enter age"))
test = input("Did you pass the driving test? (yes/no):")

if age >=18:
    if test == "Yes":
        print("License can be issued")
    else:
        print("Pass the driving test first")
else:
    print("Not eligible due to age") 

# %%
result = (45+5) * 8

print(result)

# %%
print(13+45*2)

# %%
#for loop 
# used to repeat code or iterate through a sequence by using the range.

for i in range(1,6):
    print(i)


# %%
#while loop
#use while when repitition depends on a condition
#looping through numbers 1 to 5 using while loop
i=1

while i <=5:
    print(i)
    i=i+1


# %%
#print numbers from 1 to 11
for i in range (1,11):
    print(i)



# %%
#print 1 to 10 in reverse order
for i in range(10,0,-1):
    print(i)


# %%
#print even numbers
for i in range (2,51,2):
    print(i)


# %%
#print odd numbers
for i in range (1,51,2):
    print(i)


# %%

for i in range (0,51,5):
    print(i)


# %%

#multiplication table
number = int(input("Enter number:"))

for i in range(1,11):
    print(number,"x",i,"=",number *i)


# %%
#sum of numbers from 1 to n
n = int(input("Enter n:"))

total=0

for i in range(1,n+1):
    total = total+i

print("Sum:",total)


# %%
#factorial of a number
n = int(input("Enter a number:"))

factorial = 1

for i in range(1,n+1):
    factorial = factorial*i
    print("factorial:",factorial)



# %%
#sum of even numbers from 2 to n
n=int(input("enter a number:"))
total=0
for i in range(2,n+1,2):
    total=total+i
print("sum:",total)


# %%

#count of multiple of 3
n= int(input("Enter n:"))

count=0
for i in range(1,n+1):
    if i %3==0:
         count = count +1

print("count:",count)


# %%
# sum of multiples of 5              
n= int(input("Enter  n:"))           
total=0
for i in range(1,n+1):
    if i % 5==0:
        total= total+i
print("sum:",total)

# %%
# even numbers from 2 to 50
i=2
while i <=50:
    print(i)
    i = i+2


# %%
# odd numbers from 1 to 50
i=1

while i<=50:
    print(i)
    i=i+2


# %%

# print total of numbers entered by user until 0 is emtered
total=0

number= int(input("enter a number:"))

while number!=0:
    total = total+number
    number=int(input("Enter a number:"))

print("Total:",total)
    


# %%
#password check
password="ydr123"

while password !="ydr123":
    password = int(input("Enter password: "))

print("Login successful")


# %%

#Count the numbers of digits in a number
number=int(input("Enter number:"))                                            #dry run
count = 0                                                                         #210//10=21
while (number > 0):                                                                #21//10=2
    number = number // 10                                                           #2//10=0
    count = count +1
print("Number of digits:",count)


# %%
# sum of digits in a number
number=int(input("Enter a number:"))  
total=0
while(number >0):
    digit=number % 10
    total=total + digit
    number=number // 10
print("sum of digits:",total)

# %%
# Reverse a number
number=int(input("Enter a number:"))
reverse = 0
while(number>0):
    digit=number % 10
    number= number//10
    reverse=reverse * 10 +digit
print("Reverse:",reverse)

# %%
#check if a number is a palindrome
number=int(input("Enter a number:"))
original = number
reverse=0
while(number>0):
    digit=number % 10
    reverse=reverse * 10+digit
    number=number//10
if(original==reverse):
    print("Palindrom")
else:
    print("not palindrom")

# %%
# check if a number is a prime number
number=int(input("Enter a number:"))
count=0
for i in range(1,number +1):
    if(number % i == 0):
        count=count+1
if(count==0):
    print("Prime Number")
else:
    print("Not a Prime Numnber")

# %%
#print all prime numbers between 2 to 100
number=int(input("enter a number:"))
count = 0
for number in range(1,number+1):
    count=count+1
if(count==2):
    print("prime number")
else:
    print("not  a prime")

# %%
# break
for i in range(1,11):
    if(i==5):
        break # exit the loop
print(i)

# %%
for i in range(1,11):
    if(i==5):
        continue #skip current iteration
    print(i)

# %%
for i in range(1,6):
    if(i==3):
        pass
    print(i)

# %%
age = 20
if(age >=18):
    pass  #Eligible
else:
    print("Not Eligible")

# %%
for i in range(1,11):
    if(i==7):
        print("Number Found")
        break
    print(i)

# %%
#find the largest number among 5 numbers entered by the user
largest=None

for i in range(5):
    number = int(input("Enter number:"))

    if largest is None or number >largest:
        largest = number


print("Largest:",largest)

# %%
#find the smallest number among 5 numbers entered by the user
smallest=None

for i in range(5):
    number = int(input("Enter number:"))

    if smallest is None or number < smallest:
        smallest = number


print("Smallest:",smallest)

# %%
# count the number of positive negative and zero numbers entered by the user
positive=0
negative=0
zero=0

for i in range(10):


    number = int(input("Enter a number:"))

    if number > 0:
        positive = positive +1
    elif number < 0:
        negative= negative+1
    else:
        zero = zero +1

print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero)
