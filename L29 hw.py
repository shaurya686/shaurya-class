class Vehicle:
    def __init__(self, name, fuel_consumption):  # fuel_consumption in liters per km
        self.name = name
        self.fuel_consumption = fuel_consumption

    def calculate_wage(self, distance, fuel_price):  # fuel_price in money per liter
        fuel_used = self.fuel_consumption * distance
        return fuel_used * fuel_price


class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 0.15)


class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 0.08)


# Example usage:
distance = 100  # in km
fuel_price = 1.2  # in dollars per liter

bus = Bus()
car = Car()

print(f"{bus.name} wage for {distance} km is ${bus.calculate_wage(distance, fuel_price):.2f}")
print(f"{car.name} wage for {distance} km is ${car.calculate_wage(distance, fuel_price):.2f}")
