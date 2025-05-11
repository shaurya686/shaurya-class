class Car:
    def fuel_type(self):
        raise NotImplementedError("Subclass must implement fuel_type method.")

    def max_speed(self):
        raise NotImplementedError("Subclass must implement max_speed method.")


class BMW(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"


class Lamborghini(Car):
    def fuel_type(self):
        return "Premium Petrol"

    def max_speed(self):
        return "350 km/h"


# Polymorphism in action
def show_car_info(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")
    print("-" * 20)


# Create objects
bmw = BMW()
lambo = Lamborghini()

# Show info using same method names
show_car_info(bmw)
show_car_info(lambo)
