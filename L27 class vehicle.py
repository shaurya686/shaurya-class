class vehicle:
    # create inti method
    def __init__(self, speed, mile):
        # bind the argument 
        self.max_speed = speed
        self.mileage = mile

# object cration 
bike = vehicle(240, 18)

#access the vaiable inside init method
print("model max speed:",bike.max_speed)
print("model mileage:",bike.mileage)