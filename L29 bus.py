class vehical: # parent class

    def __init__(self, nm, speed, mile):
        self.name = nm
        self.max_speed = speed
        self.mileage = mile

class bus(vehical): #child class
    pass

school_bus = bus("school volvo", 180, 12)

print("vehicle name: ", school_bus.name, "\nspeed: ", school_bus.max_speed, "\nMileage: ", school_bus.mileage)