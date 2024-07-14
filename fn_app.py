import backup

import math

books = []

def add_book():
    title = input("Enter Title: ")
    author = input("Enter Author (In case of multiple author use ',' comma ): ")
    isbn = input("Enter ISBN: ")
    published_year = input("Enter publishing year: ")
    price = input("Enter Price: ")
    quantity = input("Enter quantity: ")

    book = {
        'title': title,
        'author': author.split(","),
        'isbn': isbn,
        'published_year': published_year,
        'price': price,
        'quantity': quantity
    }

    books.append(book)

def view_all_books():
    for book in books:
        print(
            book['title'],
            book['author'],
            book['isbn'],
            book['published_year'],
            book['price'],
            book['quantity'], sep=" | "
        )

print("Wecome Wagon Library!")
menu_text = """
Your Options:
1. Add Book
2. View All books
3. Search Book by ISBN
4. Backup Books

0: Exit 
"""


while(True):
    print(menu_text)

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()
    elif choice =="2":
        view_all_books()
    elif choice == "4":
        backup.book_backup(books)
    elif choice == "0":
        break
    else:
        print("Wrong Choice!")

