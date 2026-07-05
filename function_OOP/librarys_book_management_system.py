class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)


lib = Library()

lib.add_book("Python")
lib.add_book("AI")

lib.show_books()