# Assigning variables 
name = "Mukiibi Junior"
class_name = "med class"
is_male = True
height_cm = 180

# Output variable values
print("Name:", name)
print("Stays at:", class_name)
print("Is male:", is_male)
print("Height (in cm):", height_cm)

# reassigning variables
height_m = height_cm / 100

# Updated variable values
print("Height (in meters):", height_m)

# swapping variables
z = 20
q = 40
print("\nBefore swapping: z =", z, "q =", q)
z, q = q, z
print("After swapping: z =", z, "q =", q)

# concatenating variables
sender = "Vien"
reciever = " Jay"
message = sender + ", " + reciever + ","
print("\nMessage:", message)

# Variable interpolation
price = 300
quantity = 15
total = price * quantity
print("Total:", total)

# Variable scope
def my_function():
    local_var = "Is an example of a local variable"
    print("\nHere:", local_var)

my_function()

