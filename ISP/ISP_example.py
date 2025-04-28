# BAD Code
# class Worker:
#     def work(self):
#         pass

#     def eat(self):
#         pass


# class Human(Worker):
#     def work(self):
#         return "Working..."

#     def eat(self):
#         return "Eating..."


# class Robot(Worker):
#     def work(self):
#         return "Working..."

#     def eat(self):
#         raise NotImplementedError("Robots don’t eat!")  # 🚨 Violation!


# print(Human().work())
# print(Robot().eat())


# Good Code
class Workable:
    def work(self):
        pass


class Eatable:
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        return "Working"

    def eat(self):
        return "Eating"


class Robot(Workable):
    def work(self):
        return "Working"


print(Human().eat())
print(Robot().work())
