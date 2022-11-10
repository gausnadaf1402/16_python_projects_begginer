from ast import Continue
import string
import random

characters=list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password=[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    print(password)


option=input("do you want to generate a password? (Yes/No):")

if option == "yes":
    generate_password()
elif option == "no":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input yes or no")
    quit()
