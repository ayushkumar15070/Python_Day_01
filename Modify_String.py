String  = "Hello world"
print(String.upper())

print(String.lower())


String = "Hello everyone, I am Ayush Kumar Vishwakarma i am learning python programming language to become the number one programmer in the world"
print(String.strip())

a = String.find("everyone")
if a == 6:
    print("Yes the word everyone is present in the string")
else:
    print("No there is no everyone word is present in the string")

print(String.split(" "))