# %%
#basic operators
def greet():
    print("Hello world")
    print("Welcome to python")
greet()


# %%
#Funtions with parameter
def greet(name):
    print("Hello",name)

greet("Bablu")
greet("Ravi")

# %%
#Funtions with parameters sum of two numbers
def add(a,b):
    print("Sum:",a+b)

add(10,20)
add(50,30)

# %%
#Functions with return value
#using return
def add(a,b):
    return a+b

result = add(10,20)

print(result)
#the funtion stores the value,so we can store it and use

# %%
def add(a,b):  
    return a+b

result = add(10,20)

if result > 25:
    print("Largest result")


# %%
#Funtion for even/odd
def check_even_odd(number):

    if number % 2==0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(25)

print(result)


# %%
# function for pass or fail
def check_marks(number):
    if(number >=45):
        print("Pass")
    else:
        print("Fail")
result = check_marks(45)


# %%

#funtions for largest of two numbers
def largest(a,b):
    if a>b:
        return a
    else:
        return b

result = largest(50,30)
print("Largest:",result)




# %%
# funtion + user input
def square(number):
    return number+number
number = int(input("Enter number:"))

result = square(number
                
                
                
                
                )


# %%
# funtion +loop
def multiplication_table(number):

    for i in range(1,11):
        print(number,"x",i,"=",number*i)
number = int(input("Enter a number:"))

multiplication_table(number)


# %%
#add two numbers 
def add(a,b):
    return a+b


x = int(input("Enter first number:"))
y = int(input("Enter  second number:"))

result = add(x,y)
print("Sum =",result)


# %%

#Funtion for even/odd
def check_even_odd(number):

    if number % 2==0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number:"))
print(check_even_odd(num))


# %%
# largest of three numbers
def largest (a,b,c):
    if a>=b and a>=c:
        return a
    elif b >=a and b>=c:
        return b
    else:
        return c

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))


print("Largest =",largest(a,b,c))