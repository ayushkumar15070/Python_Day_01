import datetime

x = datetime.datetime.now()

if x.year == 2026:
    print(f"Yes this is the year {x.year}")
else:
    print(f"This is not the year {x}")


print(x.year)
print(x.tzinfo)


y = datetime.datetime(1999, 8, 12, 23, 12, 23, 12222)

print(y)
print(y.strftime("%A"))