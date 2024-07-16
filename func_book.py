
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


def update_book(books):
    found_search_result = False
    search_item = input("Enter ISBN to update: ")

    found_books = []

    for index, book in enumerate(books):
        if search_item in book["isbn"]:
            found_search_result = True
            found_books.append((index, book))
            
            print(f"{len(found_books)}. Title: {book['title']} - Author(s): {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
    if not found_search_result:
        print("No book found to update.")
        return books

    try:
        selected_index = input("Enter the serial number of the book you want to update: ")
        selected_index = int(selected_index)
        
        if selected_index <= 0 or selected_index > len(found_books):
            raise IndexError

        book_index = found_books[selected_index - 1][0]

        while True:
          new_authors = input("Enter authors (Use semicolon (;) if more than 1 Author, commas are not allowed): ")
          if ',' in new_authors:
            print("You cannot use a comma in the authors field. use semicolon (;). Please try again.")
          else:
            break          
        new_year = input("Enter new publishing year: ")
        new_price = float(input("Enter new price: "))
        new_quantity = int(input("Enter new quantity: "))

        books[book_index].update({
            "authors": new_authors,
            "year": new_year,
            "price": new_price,
            "quantity": new_quantity,
        })

        save_books(books)
        print("Book updated successfully!")

    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")
    
    return books