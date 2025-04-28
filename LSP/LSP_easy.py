# Easy Refactor a Vehicle class where Car and Boat inherit, but Boat shouldn't implement drive().
class Vehicle:
    pass


class Car(Vehicle):
    def drive(self):
        return "I can drive."


class Boat(Vehicle):
    def float(self):
        return "I can float."


def let_car_drive(car: Car):
    print(car.drive())


let_car_drive(Car())
