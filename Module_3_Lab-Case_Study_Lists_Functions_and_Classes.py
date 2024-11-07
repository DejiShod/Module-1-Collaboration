class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)  
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def displayInfo(self):
        print(f"Vehicle type: {self.vehicleType}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    print("Please enter the following details for your car:")

    vehicleType = "car" 
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    car = Automobile(vehicleType, year, make, model, doors, roof)

    print("\nHere is the information about your car:")
    car.displayInfo()


if __name__ == "__main__":
    main()