import random

# creates a password with 12 characters: 4 lowercase letters, 4 uppercase letters, 2 numbers, 2 special characters. no specific order

# library of character types
lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
specialCharacters = '!@#$%&*?'

# function that generates the password according to the above specifications
def generatePassword():
    password = '' 
    while len(password) < 4:
        password += random.choice(lowerLetters)
    while len(password) < 8:
        password += random.choice(upperLetters)
    while len(password) < 10:
        password += random.choice(numbers)
    while len(password) < 12:
        password += random.choice(specialCharacters)

    password = list(password)
    random.shuffle(password)
    print(''.join(password))

# start of program
print("Welcome to the Password Generator")
print("================================")
number = input("How many passwords would you like? (up to 10)") # to do: make sure that the input is an integer less than 10. if not, prompt user to re-enter

for i in range(int(number)):
    generatePassword()
