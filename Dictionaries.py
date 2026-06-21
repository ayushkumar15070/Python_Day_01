thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 2015
}

print(thisdict)
print(type(thisdict))


questions = input("Enter your questions: ")
questions.lower()

if "does this car is belongs to ford" in  questions:
    print("Yes this car belongs to the ford brand.")
else:
    print("No, this car does no belongs to the ford.")


print(thisdict["brand"])

if "brand" in thisdict:
    print(thisdict["brand"])
else:
    print(f"No it does not exist in {thisdict}")


print(len(thisdict))



# Multiple data types

car = {
    "brand": "Ford", 
    "year" : 2015,
    "electric" : False,
    "colors" : ["red", "white", "yellow"]
}

print(car["colors"])


dict2 = dict(name = "Ayush", age = 20, country = "India")


print(dict2)