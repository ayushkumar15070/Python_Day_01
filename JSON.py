# JSON is a syntax for storing data

import json

x = '{"Name" : "John", "Age": 26, "city":"New York"}'


y = json.loads(x)
print(y)


# python to json

x = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 2015
}

z = json.dumps(x)

print(z)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))