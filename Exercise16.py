import random
def TypeOfPassword():
    type_of_password = input("What kind of password do you want?Strong, Normal, or Weak? ")
    if type_of_password == 'Strong':
        StrongPassword()
    elif type_of_password == 'Normal':
        NormalPassword()
    elif type_of_password == 'Weak':
        WeakPassword()
    else:
        type_of_password = input("Please enter a valid option")

def StrongPassword():
    password = ""
    for character in range(12):
        randnum = random.randint(32,126)
        password += chr(randnum)
    print("Your password is ",password)

def NormalPassword():
    password = ""
    for character in range(9):
        randnum = random.randint(48,126)
        password += chr(randnum)
    print("Your password is ",password)

def WeakPassword():
    password = ""
    for character in range(6):
        randnum = random.randint(65,122)
        password += chr(randnum)
    print("Your password is ",password)

TypeOfPassword()