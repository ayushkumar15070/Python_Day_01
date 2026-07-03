def changecase(func):
    def minner():
       return func().upper()
    return minner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)