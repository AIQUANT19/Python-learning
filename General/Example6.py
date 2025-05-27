# t = (1,2,3,4, 5,5)

# print(t)

# print(t[-1])
# print(t[3])
# print(f"The total count of 5 in this tuple {t} is {t.count(5)}")
# print(f"The index of 5 in this tuple {t} is {t.index(5)}")

# print(f"{t[1:]}")

# print(f"{2 in t}")
# s = (10, 20)
# print(t + s)
# print(t)
# print(t * 2)
# print(sorted(t*2))


person = {
    "name": "Alice", 
    "Age": 12,
    "grade": "A++",
    "class": 7
}
print(person["name"], person["Age"])

for key in person:
    print(key, person[key])

for key,value in person.items():
    print(f"{key}    :    {value}")

print(person.keys())  #Return all the keys
print(person.values())

print(person.items())

print(person.pop("name"))
print(person)
person["name"] = "Alice"
print(person)
print(person.clear())

print(person)