x = 34
y = "John"

print(x)
print(y)

x = 34
print(x)
x = "sally"
print(x)

# Casting
x1 = int(34)
x2 = str(34)
x3 = float(34)
print(x1)
print(x2)
print(x3)

# Get the type
print(type(x1))
print(type(x2))
print(type(x3))

myname = "Ayush" #Valid
_myname = "Ayush" #Valid
my3name = "Ayush" #Valid
print(myname)
print(_myname)
print(my3name)

# @myname = "Ayush" Invalid
# myn@me = "Ayush" Invalid


#Assigning Multiple Values
a, b, c = "Ayush", 34, "He is a genius"
print(a, b, c)


#One value to multiple variables
a1 = b1 = c1 = "Ayush"
print(a1, b1, c1)

#Unpacking a collection
Cars = ["BMW", "Audi", "Mercedes"]
Car1, Car2, Car3 = Cars
print(Car1)
print(Car2)
print(Car3)

#Combining a variables
print(Car1 + " " + Car2 + " " + Car3 + ".", "These are the cars which i am going to buy in the year 2032")

#Addition on numbers
num1 = 23
num2 = 34
print(num1 + num2)

#Subtraction on numbers
print(num1 - num2)

#Multiplication on numbers
print(num1 * num2)

#Division on numbers 
print(num1 / num2)

# Modulo operation on numbers
print(num1 % num2)

# round of figures of numbers
print(round(num1/ num2, 2))


#Global Variables 

G1 = "global variable"
def myfunc():
    G1 = "Global variable 2"
    print("This is a " + G1)

myfunc()

print("This is the " + G1)


#Creating a Gloabl Variable inside any function we use global keyword
def myfunc2():
    global G2 
    G2 = "Ayush"

    print("This is a global variable which is declared inside a function and can be used anywhere in the programme " + G2)

myfunc2()

print("Global variable which is declared inside a function definition can be accessed outside also, if we have used the global keyword in the declaration of the variable inside the function " + G2)