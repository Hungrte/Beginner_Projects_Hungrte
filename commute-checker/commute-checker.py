# Variables

distance_mi = 1
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = False

#The Main Code
if distance_mi == 0: #If distance from chosen destination is 0 then prints "Invalid Distance"
    print("Invalid Distance")
else:
    if distance_mi <= 1:    #If distance is below or equal to 1 
        if is_raining == True:  #If it is currently raining
            print('You can\'t commute going to here, it is currently raining')
        else:
            print('You can commute towards the destination')
    elif distance_mi > 6:   #If distance is more than 6
        if has_car == True or has_ride_share_app == True:   #If user has a car and has a ride share app
            print('You are able to commute to this destination')
        else:
            print('You are unable to commute to this destination')
    elif distance_mi > 1 and distance_mi <= 6:  #If distance is 2-6 miles away from destination
        if is_raining == True:  #If it is raining
            print('You cannot commute towards the destination, it is currently raining')
        else:
            if has_bike == True:    #If user has a bike
                print('You can commute towards the destination')
            else:
                print('You cannot commute to this destination due to the lack of a bike')
                
