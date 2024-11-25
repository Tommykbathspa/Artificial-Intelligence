def car_type():
              # Ask for the number of doors
    doors = int(input("How many doors does your car have? "))
    #check if doors is greater than 3
    if doors > 3:
        # Ask for ride height
        ride_height = int(input("What is the ride height of your car in millimeters? "))
        
        # Check if the ride height is greater than 190 mm
        if ride_height > 150:
            # Ask for the luggage capacity
            boot_space = int(input("What is the luggage capacity of your car in Litres? "))
            
            # Determine if it's an SUV or Crossover based on luggage capacity
            if boot_space <= 393:
                return "Crossover"
            else:
                return "SUV"
        else:
            # Ask for the luggage capacity
            boot_space = int(input("What is the luggage capacity of your car in Litres? "))
            
            # Determine if it's an Estate, Saloon or MPV
            if boot_space >= 575:
                #Ask for passenger capacity
                passengers_num = int(input("How many passengers can your car hold? ")) 

                  # Determine if it's an Estate or MPV
                if passengers_num > 5:
                    return "MPV"
                else:
                    return "Estate"  
            else:
                return "Saloon"
    
    # If the car has 3 or fewer doors
    else:
        # Ask for the luggage capacity
        boot_space = int(input("What is the luggage capacity of your car in Litres? "))
        
        # Determine if it's a Hatchback or City
        if boot_space >= 280:
            return "Hatchback"
        else:
            return "City"

# Print car type
print("Your car is a " + car_type())


#ChatGPT helped to fix errors in this code as i created it 
