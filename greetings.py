
name = input("What's your name? ")

print ("Hello " + name + " I am your phonebook")

while True:
    age = input("How old are you?  ")
    try:
        age = int(age)
        break
    except ValueError:
        print("That doesn't seem to be an integer.")

if age < 18:
    print("You are so young! Life is ahead of you!")
elif age >=18 and age <=40 : 
    print ("That's a nice age")
else:
    age<=40
    print("you must be very wise!")    

