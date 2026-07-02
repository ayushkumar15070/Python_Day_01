def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 400 
    def myinnerfunc():
       print(x)
    myinnerfunc()

myfunc()



x = 200

def myfunction():
    print(x)

myfunction()


x = 23

def my_function():
    x = 34
    print(x)

my_function()

print(x)


def anotherfunction():
    global x
    x = 34
    print(x)

anotherfunction()
print(x)