dict1 = {
    "brand" : "Ford", 
    "Model" : "Mustang",
    "year" : 2015
}

x = dict1["brand"]
print(x)


# by using the get method

y = dict1.get("Model")
print(y)


# Key method will return all the keys present in it 
z = dict1.keys()
print(z)

car = {
    "Brand" : "BMW",
    "Model" : "M8",
    "Year" : 2019
}

x = car.keys()
print(x)

car["color"] = "Blue"

print(x)