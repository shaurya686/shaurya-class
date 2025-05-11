class Vehicle:
    all_burnt = []

    def __init__(self, name):
        self.name = name
        self.is_burnt = False

    def burn(self):
        if not self.is_burnt:
            self.is_burnt = True
            Vehicle.all_burnt.append(self)
            print(self.burn_message())
        else:
            print(f"{self.name} is already burnt.")

    def burn_message(self):
        return f"{self.name} is burning!"


class Car(Vehicle):
    def burn_message(self):
        return f"{self.name} (Car) explodes into flames!"

class Plane(Vehicle):
    def burn_message(self):
        return f"{self.name} (Plane) crashes and burns!"

class Train(Vehicle):
    def burn_message(self):
        return f"{self.name} (Train) melts on the tracks!"

class Bus(Vehicle):
    def burn_message(self):
        return f"{self.name} (Bus) goes up in smoke!"


def burn_all(vehicles):
    for v in vehicles:
        v.burn()

def show_burnt_vehicles():
    print("\nBurnt Vehicles:")
    for v in Vehicle.all_burnt:
        print(f"- {v.name}")


# Example
vehicles = [
    Car("Lamborghini"),
    Plane("Jet A1"),
    Train("Express Line"),
    Bus("City Bus")
]

burn_all(vehicles)
show_burnt_vehicles()
