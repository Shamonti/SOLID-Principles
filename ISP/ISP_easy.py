# Bad design
# class Machine:
#     def print(self):
#         raise NotImplementedError

#     def scan(self):
#         raise NotImplementedError

#     def fax(self):
#         raise NotImplementedError


# print(Machine.scan())
# Tasks:

# Split it properly so that a simple Printer class doesn’t need to implement scan() or fax().


# Good Design
class Printable:
    def print(self):
        pass


class Scanable:
    def scan(self):
        pass


class Faxable:
    def fax(self):
        pass


class Printer(Printable):
    def print(self):
        return "Printing"


print(Printer().print())
