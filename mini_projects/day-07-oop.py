class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print("Title :", self.title)
        print("Author:", self.author)


book1 = Book("Harry Potter", "J.K. Rowling")

book1.show()