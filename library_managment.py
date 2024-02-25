class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        print("♦ Available books ♦")
        sayaç=0
        for book in books:
            title, author, release_date, num_pages = map(str.strip, book.split(','))
            print(f"*** Title: {title}, Author: {author}")
            sayaç+=1
        if sayaç==0:
            print("*** No Available Books Right Now ***")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("*** Book Added ***")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        updated_books = [book for book in books if title_to_remove not in book.split(',')]
        self.file.truncate(0)
        self.file.seek(0)
        for updated_book in updated_books:
            self.file.write(f"{updated_book}\n")
        print("*** Book removed ***")

# Created an object named "lib" with "Library" class
lib = Library()

print("♦♦♦♦♦♦♦ WELCOME TO THE  LIBRARY ♦♦♦♦♦♦♦\n")
print("*** MENU ***")
print("1) List Books")
print("2) Add Book")
print("3) Remove Book")
print("Q) Quit")
while True:
    try:
        choice = input("Enter your choice (1/2/3/Q): ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice.upper() == "Q":  # Convert input to uppercase for case-insensitivity
            print(("♦ Quited ♦"))
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or Q.")
    except:
        print("Invalid choice. Please enter 1, 2, 3, or Q.")
