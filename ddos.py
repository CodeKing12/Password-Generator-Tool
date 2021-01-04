# Password Generator Tool
import csv
import random

alphabets = "abcdefghijklmnopqrstuvwxyz"
block_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symb_list = "!@#$%^&*()_-\\/:{}[]><?"
ran = range(0, 10)
task = input("Reply with \"1\" if you want to generate a password and with \"2\" if you want to retrieve a password: ")
password_dict = {}
password_list = []
word_pass = []
password = ""
def generate_password(website, digit_length, symbols, capitals):
    global password
    digiter = digit_length
    while digiter > 0:
        if symbols == "No" and capitals == "No":
            if ((digit_length % 2) == 0):
                num_letters = int(digit_length / 2)
                num_numbers = int(digit_length / 2)
            if ((digit_length % 2) != 0):
                num_numbers = int(digit_length / 2)
                num_letters = digit_length - num_numbers
            word = random.choices(alphabets, k=num_letters)
            first = 0
            if ((word in password_list) == False) and len(password_list) == 0:
                for letter in word:
                    password_list.append(letter)
            num = random.choices(ran, k=num_numbers)
            if ((num in password_list) == False) and len(password_list) == num_letters:
                for number in num:
                    password_list.append(str(number))
            random.shuffle(password_list)
            password = "".join(password_list)


        if symbols == "Yes" and capitals == "No":
            num_symbols = int(int(digit_length / 2) / 2)
            remainder = digit_length - num_symbols
            if ((remainder % 2) == 0):
                num_letters = int(remainder / 2)
                num_numbers = int(remainder / 2)
            if ((remainder % 2) != 0):
                num_numbers = int(remainder / 2)
                num_letters = remainder - num_numbers
            word = random.choices(alphabets, k=num_letters)
            if ((word in password_list) == False) and len(password_list) == 0:
                for letter in word:
                    password_list.append(letter)
            num = random.choices(ran, k=num_numbers)
            if ((num in password_list) == False) and len(password_list) == num_letters:
                for number in num:
                    password_list.append(str(number))
            symb = random.choices(symb_list, k=num_symbols)
            if ((symb in password_list) == False) and len(password_list) == remainder:
                for symbol in symb:
                    password_list.append(symbol)
            random.shuffle(password_list)
            password = "".join(password_list)

        if symbols == "No" and capitals == "Yes":
            if ((digit_length % 2) == 0):
                num_letters = int(digit_length / 2)
                num_numbers = int(digit_length / 2)
            if ((digit_length % 2) != 0):
                num_numbers = int(digit_length / 2)
                num_letters = digit_length - num_numbers
            num_capitals = int(num_letters / 2)
            num_littles = num_letters - num_capitals
            word = random.choices(alphabets, k=num_littles)
            cap_word = random.choices(block_alphabets, k=num_capitals)
            if ((word in password_list) == False) and len(password_list) == 0:
                for letter in word:
                    password_list.append(letter)
            if ((cap_word in password_list) == False) and len(password_list) == num_littles:
                for cap_letter in cap_word:
                    password_list.append(cap_letter)
            num = random.choices(ran, k=num_numbers)
            if ((num in password_list) == False) and len(password_list) == num_letters:
                for number in num:
                    password_list.append(str(number))
            random.shuffle(password_list)
            password = "".join(password_list)

        if symbols == "Yes" and capitals == "Yes":
            num_symbols = int(int(digit_length / 2) / 2)
            remainder = digit_length - num_symbols
            if ((remainder % 2) == 0):
                num_letters = int(remainder / 2)
                num_numbers = int(remainder / 2)
            if ((remainder % 2) != 0):
                num_numbers = int(remainder / 2)
                num_letters = remainder - num_numbers
            num_capitals = int(num_letters / 2)
            num_littles = num_letters - num_capitals
            word = random.choices(alphabets, k=num_littles)
            if ((word in password_list) == False) and len(password_list) == 0:
                for letter in word:
                    password_list.append(letter)
            num = random.choices(ran, k=num_numbers)
            cap_word = random.choices(block_alphabets, k=num_capitals)
            if ((cap_word in password_list) == False) and len(password_list) == num_littles:
                for cap_letter in cap_word:
                    password_list.append(cap_letter)
            if ((num in password_list) == False) and len(password_list) == num_letters:
                for number in num:
                    password_list.append(str(number))
            symb = random.choices(symb_list, k=num_symbols)
            if ((symb in password_list) == False) and len(password_list) == remainder:
                for symbol in symb:
                    password_list.append(symbol)
            random.shuffle(password_list)
            #global password
            password = "".join(password_list)
        digiter -= 1

    print("""
    Your new password is {password}
    """.format(password=password))
    question = input("Would you like to keep it? ")
    if question == "Yes":
      with open("passwords.csv", "a") as passwords:
        fieldnames = ["website", "password"]
        passwords_file = csv.DictWriter(passwords, fieldnames = fieldnames)
        passwords_file.writeheader()
        passwords_file.writerow({"website": website, "password": password})
      print("""
      Your password '{password}' for the website '{website}' has been saved successfully""".format(website=website, password=password))
    elif question == "No":
      generate_password(website, digit_length, symbols, capitals)
    else:
        print("INVALID RESPONSE!!")

if task == "1":
    website = input("What website do you want create a password for? ")
    digit_length = int(input("How many characters do you want your password to have? "))
    symbols = input("Do you want your password to have symbols (!@#$%^)? Reply(Yes/No) ")
    capitals = input("Do you want to include capital letters in your password? Reply(Yes/No) ")
    generate_password(website, digit_length, symbols, capitals)
if task == "2":
    diction = {}
    with open("passwords.csv") as passwords:
        passwar = csv.DictReader(passwords)
        for row in passwar:
            if row["website"] != "website":
                diction[row["website"]] = row["password"]
    specify = input(
        "Reply '1' if you have a specific website you want to retrieve and reply '2' if you want to view all your passwords: ")
    if specify == "1":
        site_retrieve = input("Which website's password would you like to retrieve? Please make no mistakes: ")
        if ((site_retrieve in diction) == True):
            print("Your password for '{site}' is '{passtw}'".format(site=site_retrieve, passtw=diction[site_retrieve]))
        else:
            print("You have not created a password for that particular website yet. ")
    if specify == "2":
        for website, password in diction.items():
            print("Your password for '{site}' is '{word}'".format(site=website, word=password))





#make the code above into a function so that you can call it when the answer is no
#make a process for the reply 2:
#add features when you remember them
#add finishing touches
