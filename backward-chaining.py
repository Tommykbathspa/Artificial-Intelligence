def ask_question(question, valid_answers=None):
    answer = input(question)
    if valid_answers:
        while answer not in valid_answers:
            print("Invalid answer. Please try again.")
            answer = input(question)
    return answer

def is_suv():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number >= 4:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height >= 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space > 393:
                return True
            else:
                return False
    return False

def is_crossover():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number == 5:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height >= 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space <= 393:
                return True
            else:
                return False
    return False

def is_estate():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number == 5:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height < 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space >= 575:
                passengers_num = int(ask_question("How many passengers can your car hold? "))
                if passengers_num <= 5:
                    return True
            return False
    return False

def is_mpv():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number == 5:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height < 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space >= 575:
                passengers_num = int(ask_question("How many passengers can your car hold? "))
                if passengers_num > 5:
                    return True
            return False
    return False

def is_saloons():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number == 4:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height < 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space < 575:
                return True
            return False
    return False

def is_hatchback():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number >= 3:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height < 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space <= 280:
                return True
            return False
    return False

def is_city():
    door_number = int(ask_question("How many doors does your car have? "))
    if door_number == 3:
        ride_height = int(ask_question("What is the ride height of your car in millimeters? "))
        if ride_height < 150:
            boot_space = int(ask_question("What is the luggage capacity of your car in Litres? "))
            if boot_space > 280:
                return True
            return False
    return False


def car_type():
    car_type = ask_question("What car type do you want to check (SUV, Crossover, Estate, MPV, Saloon, Hatchback, City)? ", 
                             valid_answers=["SUV", "Crossover", "Estate", "MPV", "Saloon", "Hatchback", "City"]) #valid answers line made with ChatGPT

    if car_type == "SUV":
        if is_suv():
            return "SUV"
        else:
            return "Not an SUV"

    elif car_type == "Crossover":
        if is_crossover():
            return "Crossover"
        else:
            return "Not a Crossover"

    elif car_type == "Estate":
        if is_estate():
            return "Estate"
        else:
            return "Not an Estate"

    elif car_type == "MPV":
        if is_mpv():
            return "MPV"
        else:
            return "Not an MPV"

    elif car_type == "Saloon":
        if is_saloons():
            return "Saloon"
        else:
            return "Not a Saloon"

    elif car_type == "Hatchback":
        if is_hatchback():
            return "Hatchback"
        else:
            return "Not a Hatchback"

    elif car_type == "City":
        if is_city():
            return "City"
        else:
            return "Not a City"

# Print car type
print("Your car is: " + car_type())



