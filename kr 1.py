class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        print( f"{self.brand} {self.model}, year {self.year}, mileage {self.mileage} km")

    def drive(self, km):
        self.mileage += km

    def is_old(self):
        return self.year < 2015



class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def drive_all(self, km):
        for car in self.cars:
            car.drive(km)

    def show_all(self):
        for car in self.cars:
            print(car.info())


    def show_old_cars(self):
        for car in self.cars:
            if car.is_old():
                print(car.info())


car1 = Car("BMW", "CSL", 2022, 25000)
car2 = Car("Volkswagen", "Passat", 2012, 120000)
car3 = Car("Mercedes", "c 63", 2015, 80000)

garage = Garage()
garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)


print("Всі машини:")
garage.show_all()

print("Старі машини:")
garage.show_old_cars()

