my_dictionary={
    "name":"Deepak",
    "Age": 25,
    "sex":"M",
    "Martial Status":"Single"
}

my_dictionary["company"]="Orange Business"

for key in my_dictionary:
    print(key,":",my_dictionary[key])

print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.fromkeys("name"))


