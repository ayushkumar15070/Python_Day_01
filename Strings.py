print("Hello, world!")
print('Hello, world!')

x = "Hello, world!"
print(x)

# Multiline Strings

Number_one_coder = """Hello everyone i am Ayush Kumar Vishwakarma learning
python language to become the number one coder in the world 
and to build things that are beyond human limits"""

print(Number_one_coder)

#Strings are Arrays

Fruit = "Banana"
for i in range(1, len(Fruit) + 1):
    print(i)

print(Fruit[1])

print(len(Fruit))


#In keyword to check whether a specific word is there in the string or not 

cars = "BMW makes the best car in the world"
print("best" in cars)

# by using if else statement

if "best" in cars:
    print("Yes the word \"best\" is present in the cars")


# Not statement 
billionaire = "Elon Musk is the trillionaire now"
if "trillionaire" not in billionaire:
    print("Trillionaire not present in the statement")
else:
    print("Trillionaire present in the statement")