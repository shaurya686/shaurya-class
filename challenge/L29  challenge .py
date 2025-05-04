class Vehicle:
    def __init__(self, name, fuel_consumption):  # liters per km
        self.name = name
        self.fuel_consumption = fuel_consumption

    def calculate_wage(self, distance, fuel_price):  # km and price per liter
        fuel_used = self.fuel_consumption * distance
        return fuel_used * fuel_price


class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 0.15)  # example: 0.15 L/km


class Train(Vehicle):
    def __init__(self):
        super().__init__("Train", 0.25)  # example: 0.25 L/km


class Plane(Vehicle):
    def __init__(self):
        super().__init__("Plane", 3.5)  # example: 3.5 L/km


# Example usage:
distance = 200  # km
fuel_price = 1.5  # per liter

bus = Bus()
train = Train()
plane = Plane()

print(f"{bus.name} wage for {distance} km = ${bus.calculate_wage(distance, fuel_price):.2f}")
print(f"{train.name} wage for {distance} km = ${train.calculate_wage(distance, fuel_price):.2f}")
print(f"{plane.name} wage for {distance} km = ${plane.calculate_wage(distance, fuel_price):.2f}")
