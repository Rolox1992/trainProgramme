# Coding challenge
capacity = 5

# Ask user their age
age = int(input("Enter your age: "))

# Check if there is seat available
if capacity > 0:
    if age < 12:
        print("Sorry, under 12's are not allowed to ride this train")

    elif age <= 12 <= 17:
        school_id = input("Do you have your id card? (Y/N): ")
        if school_id == "Y":
            previous_rides = int(input("Enter the number of previous rides: "))

            if previous_rides < 3:
                print("You can ride the train, enjoy it")
                capacity = capacity - 1

            else:
                print("Sorry, minors are restricted to 3 rides on the train")

        else:
            print("Sorry, minor between those ages must present their ID")

    elif age > 17:
        print("You can ride the train, enjoy it")
        capacity = capacity - 1

else:
    print("Sorry the train is full")
