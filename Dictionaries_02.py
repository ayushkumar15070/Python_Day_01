car = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 2015
}

car["Model"] = "Endavour"
print(car)

car.update({"Year" : 2001})
print(car)

car["Color"] = "Blue"
print(car)

newcar = {

}

# name = input("Enter the car name: ") 
# model = input("Enter the model name: ")
# year = int(input("Enter the year of the car: "))
# color = input("Enter the color of the car: ")

# newcar.update({"Brand" : name, "Model": model, "year" : year, "color": color})
# print(newcar)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

