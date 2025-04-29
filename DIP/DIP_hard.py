# 🎯 Hard Challenge: Logger System
# Build an abstract Logger class with method log(message).

# Implement:

# ConsoleLogger (print to console)

# FileLogger (write to a file)

# Create an Application class that uses a Logger.

# Demonstrate switching between ConsoleLogger and FileLogger without touching Application logic.

# ✅ Bonus: (If you want extra ✨) make the file logger write to log.txt.

from abc import ABC, abstractmethod


# 1. Abstract Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> str:
        pass


# 2. Concrete Implementation
class ConsoleLogger(Logger):
    def log(self, message: str) -> str:
        print(f"Printing to console: {message}")
        return "Logging to console."


# class FileLogger(Logger):
#     def log(self, message: str) -> str:
#         return f"Writing to a file: {message}"


class FileLogger(Logger):
    def log(self, message: str) -> str:
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")
        return "Logging in file."


# 3. High level service depends on abstraction
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def apply_log(self, message: str) -> str:
        return self.logger.log(message)


# console_logger = Application(ConsoleLogger())
# print(console_logger.apply_log("Welcome to the console!"))


file_logger = Application(FileLogger())
print(file_logger.apply_log("Welcome to my file!"))
