# Code without SRP
# class Book:
#   def __init__(self, title, author):
#     self.title = title
#     self.author = author
  
#   def save_book(self):
#     print(f"Saving {self.title} to file.")
  
#   def print_summary(self):
#     print(f"Summary: {self.title} by {self.author}")

# book = Book("Harry Potter", "J.K Rowling")
# book.save_book()
# book.print_summary()

# Code with SRP
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class BookFileHandler:
  def save(self, book):
    print(f"Saving {book.title} to file.")

class BookSummary:
  def summary(self, book):
    print(f"Summary: {book.title} by {book.author}")

book = Book("Harry Potter", "J.K Rowling")
file_handler = BookFileHandler()
summary = BookSummary()
file_handler.save(book)
summary.summary(book)