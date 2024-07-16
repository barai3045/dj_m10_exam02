from func_file_operation import save_books, save_lents


def lend_books(books, books_lend):
    found_search_result = False
    search_item = input("Enter title or ISBN or author's name to lend Book: ")
    matching_books = []
  
    for index, book in enumerate(books):
        if (search_item.lower() in book["authors"].lower() or 
            search_item.lower() in book["title"].lower() or 
            search_item in book["isbn"]):
      
            found_search_result = True
            matching_books.append((index, book))
      
            print(f"{len(matching_books)}. Title: {book['title']} - Author(S): {book['authors']} - ISBN: {book['isbn']} -Price: {book['price']} - Quantity: {book['quantity']}")
      
      
    if not found_search_result:
        print("No book found to lend.")
        return books_lend
  
    try:
        selected_index = input("Enter the serial number of book which you want to lend: ")
        selected_index = int(selected_index)
    
        if selected_index <= 0 or selected_index > len(matching_books):
            raise IndexError

        book_index = matching_books[selected_index - 1][0]
    
    
        borrower = input("Enter borrower's name: ")
    
        if int(books[book_index]["quantity"]) > 0:
      
            remaining_quantity = int(books[book_index]["quantity"]) - 1
      
            borrowed_book = books[book_index]["title"]
      
            book_isbn = books[book_index]["isbn"]
      
    
            books[book_index]["quantity"] = str(remaining_quantity)
      
            books_lend.append({
                "title": borrowed_book,
                "borrower": borrower,
                "isbn" : book_isbn,
                })
      
            print(f"{borrower} successfully borrowed '{borrowed_book}' book! ")
      
            save_lents(books_lend)
            save_books(books)
      
        else:
            print("Not enough books available to lend")
    
    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")

    return books_lend


def view_books_lend(books_lend):
    if not books_lend:
        print("No books have been lent.")
    else:
        print("Lent Books: ")
        for book in books_lend:
            print(f"Title: {book['title']} - Borrower: {book['borrower']} - ISBN: {book['isbn']}")



def books_return(books, books_lend):
    if not books_lend:
        print("No books have been lent.")
        return
  
    found_search_result = False
    search_item = input("Enter ISBN of the book to return: ")
  
    for index, book in enumerate(books_lend):
        if search_item == book["isbn"]:
            found_search_result = True
            print(f"{index+1}. Title: {book['title']} - Borrower: {book['borrower']} - ISBN: {book['isbn']}")
      
    if not found_search_result:
        print("No lent book found.")
        return  
  
    try:
        selected_index = input("Enter the serial number of the book you want to return: ")
        selected_index = int(selected_index)
    
        if selected_index <= 0 or selected_index > len(books_lend):
            raise IndexError
    
        lent_book = books_lend[selected_index - 1]
        books_lend.pop(selected_index - 1)
    
        for book in books:
      
            if book["isbn"] == lent_book["isbn"]:
        
                book["quantity"] = str(int(book["quantity"]) + 1)
        
                print(f"'{lent_book['title']}' successfully returned by {lent_book['borrower']}.")
                save_lents(books_lend)
                save_books(books)
                break
    
    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct serial number.")
    
    return books_lend            