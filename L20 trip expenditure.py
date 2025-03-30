def hotel_cost(nights):
    return 140*nights
 
#difine a function called plane_ride_cost that takes a string ,citys as input>
def plane_ride_cost(city):
    if "charlottle" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
    elif "london" == city:
        return 275
    
#define a function called rental_car_cost with an argument da, mone and city
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) +