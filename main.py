from book_class import Book
from func_lend import books_return, lend_books, view_books_lend
from func_book import add_book, view_books, delete_book, update_book
from func_file_operation import restore_books, restore_books_lend
from func_search import search_by_title_isbn, search_by_authors



menu_text = """
    Library Management System
    1. Add Book
    2. View All Books
    3. Search Books(Title or ISBN only)
    4. Search Books by Author
    5. Update Book
    6. Remove Book
    7. Lend Book
    8. View Lent Book
    9. Return Book
    0: Exit
"""




def main():
    books = []
    books_lend = []
    restore_books(books)
    restore_books_lend(books_lend)
    while True:
        print(menu_text)
        
        choice = input("Enter your choice: ")
        if choice =="1":
            books = add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_by_title_isbn(books)
        elif choice == "4":
            search_by_authors(books)
        elif choice == "5":
            books = update_book(books)
        elif choice == "6":
            books = delete_book(books, books_lend)
        elif choice == "7":
            books_lend= lend_books(books, books_lend)
        elif choice == "8":
            view_books_lend(books_lend)
        elif choice == "9":
            books_lend = books_return(books, books_lend)
        elif choice == "0":
            print('Thank You for Using!')
            break
        else:
            print("Invalid choice. Please choose Correct Input")



main()






