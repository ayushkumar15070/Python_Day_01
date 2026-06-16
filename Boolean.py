print(2>3)
print(3<4)
print(4>3)

a = 2
b = 3

if (a > b):
    print("a is greater than b")
else:
    print("b is greater than a")\
    

print(bool("hello"))
print(bool(34))


# function returning boolean
def myfunc():
    return True

print(myfunc())

def myfunction():
    return True

if myfunction:
    print("Yes")
else:
    print("No")

# Built in boolean determining function

x = 23
print(isinstance(x, int))