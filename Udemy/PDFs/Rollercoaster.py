# This code checks the height of a person and determines if they can ride the rollercoaster or not.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")

    elif age <= 18:
        bill = 7
        print("Please pay $7.")

    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is gonna be okay. Have a free ride!.")

    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a Photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        print("Please pay $3.")
    else:
        print("No Photo taken.")

    print("Your total bill is $" + str(bill))
else:
    print("Sorry, you need to be taller to ride the rollercoaster.")


