while True:
    your_name = input("What is your good name?")
    your_age = input("What is your age?")
    your_height = input("Enter your height value")
    fav_drink = input("What is your favorite drink?")
    fav_food = input("What would you love to eat?")

    while True:
        answer =str(input("Run program again? (Y/N):"))
        if answer in ("Y","N"):
            break
        print("Invalid input.")
    if answer == "Y":
        continue
    else:
        print("Goodbye")
        break

print("Your name is" + your_name + ".")    
print("You are " + str(your_age) +"years old")  
print("You are " + str(your_height) + "tall") 
print (fav_drink+" is your anytime drink")
print(fav_food + " is what you prefer eating most of the time?")

