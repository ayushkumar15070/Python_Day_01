# Text type : str
# numeric type : int, float, complex
# sequence type : list, tuple, range
# mapping type : dict
# set type : set, frozenset
# Boolean type : bool : True and False
# Binary type : bytearray, bytes, memoryview
# Nonetype : Nonetype


x = "Hello World" # String type or str
x = 20 #Numeric type or int
x = 20.5 #Numeric type or float
x = 1j #Numeric type of complex
x = ["Apple", "banana", "cherry"] #list type
x = ("apple", "banana", "cherry") #tuple type
x = range(6) #range type
x = {
    "name": "John",         #dictionary type
    "age": 36
}
x = {"apple", "banana", "cherry"} #set type
x = frozenset({"apple", "banana", "cherry"}) #frozenset type
x = True or False #Boolean type 
x = b"hello" #bytes type
x = bytearray(5) #bytearray type
x = memoryview(bytes(5)) #memoryview type
x = None #NoneType 



#Setting the specific Data Type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple","banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name = "John", age = 36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))