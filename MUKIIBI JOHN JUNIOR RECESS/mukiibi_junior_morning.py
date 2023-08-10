#control flow
#conditional statements (if, elif, else)

""" if condition1:
    print('True') #code lock is only executed if condition is true
elif condition2:
    print('True') #code lock is only executed if condition is true
else:
    print('False') #code lock is only executed if conditions are false

 """
 #age<18, print "You are underage"
 #age>= 18 and <= 65 "You are adult"
 #print "You are a senior citizen"
age = 67
if age<18:
    print("You are underage")
elif age>=18 and age<=65:
    print("You are adult")  
else:
    print("You are a senior citizen")  

#Loops
#Loops (for , while)
#for loop
#for x in sequence: #for items in a sequence
fruits = ["watermelon", "banana", "pears"]
for fruit in fruits:
    print(fruit)

#while loop
#while condition is true, it will execute
#example
x = 0
while x < 10:
    print(x)
    x += 1

fruits = ["watermelon", "banana", "pears"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1 

#Break and continue statements
#Break statement
for number in range(1,10):
    if number == 5:
        break
    print(number)

#continue statement
for y in range(1,10):
    if y == 2:
        continue
    print(y)

#Exception handling(try, except, finally)
#try block: used when raising an exception 
# except: used to handle specific exceptions that occur
#finally: executes the code after the exception is handled
try:
    x = 10/0
except ZeroDivisionError:
    print('Error: Division by zero') #cannot divide by zero
finally:
    print('This is always executed') #complete execution  

emotions = {
    "happy" : "I am glad to hear that you are happy",
    "sad" : "I am sorry to hear that you are feeling sick",
    "angry" : "Take a deep breath and try to stay alive",
    "fearful" : "I understand that fear can be very challenging"
}
#Prompt the user to enter their emotions
user = input("how are you feeling today?")
#convert the user input to lowercase
user = user.lower()
if user in emotions:
    print(emotions[user])

#Exercise
#write a program to ask students about their mental health
#prompt students on a scale of 1 to 10 to rate their mental health
# Dictionary to store student responses
responses = {}

# Number of students
while True:
    try:
        num_students = int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Ask each student about their mental health
for i in range(1, num_students + 1):
    student_name = input(f"Enter the name of student {i}: ")

    while True:
        try:
            mental_health_rating = int(input("On a scale of 1 to 10, rate your mental health: "))
            if mental_health_rating < 1 or mental_health_rating > 10:
                print("Invalid rating. Please enter a number between 1 and 10.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Store the response in the dictionary
    responses[student_name] = mental_health_rating

# Display the responses
print("\nMental Health Ratings:")
for student, rating in responses.items():
    print(f"{student}: {rating}")
