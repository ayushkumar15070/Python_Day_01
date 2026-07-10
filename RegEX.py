# A RegEX or regular expression is a sequence of characters that forms a seafch pattern

import re

txt = "The rain in Spain"
x = re.search("The rain", txt)

print(x)

x = re.findall("ai", txt)
print(x)


print(x)


z = re.split("\s", txt, 1)
print(z)