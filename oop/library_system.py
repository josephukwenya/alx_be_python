class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"Book: {self.title} by {self.author}"
  
# Derived class: Ebook
class EBook(Book):
  def __init__(self, title, author, size):
    super().__init__(title, author)
    self.size = size

    def __str__(self):
      return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class: printbook
class PrintBook(Book):
  def __init__(self, title, author, page_count):
    super().__init__(title, author)
    self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
# composition: library class
class Library:
  def __init__(self):
    self.books = []


  def add_book(self, book):
    self.book.append(book)

  def list_books(self):
    for book in self.books:
      print(book)