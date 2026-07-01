def greeting(name):
    return "Hello " + name

name = input("Enter your name: ")
print(greeting(name))



def greetings(fname, lname, mname = ""):
    if(mname == ""):
        return f"Hello {fname} {lname}"
    else:
        return f"Hello {fname} {mname} {lname}"
    

fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")

if(mname == ""):
    sentence = greetings(fname, lname)
    print(sentence)
else:
    sentence = greetings(fname, lname, mname)
    print(sentence)
    