#STRINGS
#exercise one: use the len() function to determine the length of the string
a = "Junior"
length = len(a)
print("The length of the string: " + str(length))
#exercise two: use a for loop in a string
for char in a:
    print(char)
#exercise three: slicing in a string
b = "Good Morning!"
c = b[6:8] 
print(c)  
d = b[-3:-2] 
print(d)  
e = b[::3] 
print(e)  
f = b[::-1] 
print(f) 


#BOOLEAN
#exercise: use a condition to show how to use booleans
is_raining = True
has_umbrella = False

# Condition using booleans
if is_raining and not has_umbrella:
    print("It's raining and you don't have an umbrella. Stay indoors.")
elif is_raining and has_umbrella:
    print("It's raining, but you have an umbrella. Enjoy your walk!")
else:
    print("It's not raining. Have a great day!")

#DICT
my_dict1 = {
    "book": "Life in a year",
    "writer": "Johnsons",
    "published": 2040
}
#Exercice one: use the values () method to return a list of values for the dictionary
print(my_dict1.values())
#Exercise two: check if a key exists in the dictionary
#using in operator
if "book" in my_dict1:
    print("Key 'book' exists in the dictionary.")
else:
    print("Key 'book' does not exist in the dictionary.")
#using dict.get() method
if my_dict1.get("writer") is not None:
    print("Key 'writer' exists in the dictionary.")
else:
    print("Key 'writer' does not exist in the dictionary.")
#Exercise three: how to change items, how to update
# Update values using the 'update()' method
my_dict1.update({"location": "Chicago", "street": "11th street"})
print(my_dict1)
#Exercise four: how to add items, how to remove items
my_dict1.pop("published") 
print(my_dict1)
my_dict1.popitem() 
print(my_dict1)
my_dict1.clear() 
print(my_dict1)
#how to add items
my_dict1["shoes"] = "Air Jordans"
print(my_dict1)
#Exercise five:how to loop through the dictionary and how to nest the dictionary
for key, value in my_dict1.items():
    print(key, "->", value)
#how to nest the dictionary
my_dict2 = {
    "name": "Junior",
    "age": {
        "2023": 20,
        "2030": 30
    },
    "shoe_size": 40
}
# Accessing nested values
print(my_dict2["age"]["2023"])
print(my_dict2["age"]["2030"])    


#NUMBERS
x = 23 #int
y = 3.14 #float
z = 2-3j #complex
#convert from int to complex
g = complex(x)
print(g)
print(type(g))
#convert from float to complex
h = complex(y)
print(h)
print(type(h))
#convert from int to float
k = float(x)
print(k)
print(type(k))
#convert from complex to float
m = float(z.real)
print(m)
print(type(m))
n = float(z.imag)
print(n)
print(type(n))
