def book_backup(books):
    #take all contact and write then into a file
    
    with open("books.csv", "wt") as fp:
        for book in books:
            book_line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['published_year']}, {book['price']}, {book['quantity']}"
            fp.write(book_line)
    
    print("Book backup successfully!")

