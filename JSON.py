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