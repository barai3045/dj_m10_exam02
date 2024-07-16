
from func_file_operation import save_books


def add_book(books):
    print("Enter Book detail:")
    title = input("Title: ")

    authors = input("Author(s) (for multiple author use ';' semiclone): ").split(';')

    isbn = input("ISBN: ")
    year = input("Publishing year: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }
    
    books.append(book)
    save_books(books)   
    return books   

def view_books(books):
    for book in books:
        print(
            f"Title: {book['title']}, Authors: {(book['authors'])} ,  ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: { book['quantity']}" 
        )

def delete_book(books, lent_books):
    found_search_result = False
    search_item = input("Enter ISBN to remove: ")

    found_books = []

    for index, book in enumerate(books):
        if search_item in book["isbn"]:
            
            found_search_result = True
            found_books.append((index, book))
            
            print(f"{len(found_books)}. Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
        if not found_search_result:
            print("No book found to remove.")
            return books
    
    try:
        selected_index = input("Enter the serial number of the book which you want to delete: ")
        selected_index = int(selected_index)
        
        if selected_index <= 0 or selected_index > len(found_books):
            raise IndexError

        book_index = found_books[selected_index - 1][0]
        book_to_delete = books[book_index]

        # check for lending
        for lent_book in lent_books:
            if lent_book['isbn'] == book_to_delete['isbn']:
                print(f"Cannot delete '{book_to_delete['title']}' because it is currently borrowed.")
                return books
        
        ## if not lended
        books.pop(book_index)
        save_books(books)
        print(f"'{book_to_delete['title']}' has been deleted successfully.")
        
    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")
    
    return books
