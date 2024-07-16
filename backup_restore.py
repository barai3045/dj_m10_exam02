def book_backup(books):
    #take all contact and write then into a file
    
    with open("books.csv", "wt") as fp:
        for book in books:
            book_line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['published_year']}, {book['price']}, {book['quantity']}"
            fp.write(book_line)
    
    print("Book backup successfully!")



def book_restore(books):
    books.clear()

    with open("books.csv", "r") as fp:
        for line in fp.readlines():
            line_splitted = line.split(",")
            book = {
                'title': line_splitted[0],
                'author': line_splitted[1],
                'isbn': line_splitted[2],
                'published_year': line_splitted[3],
                'price': line_splitted[4],
                'quantity': line_splitted[5]
            }
            books.append(book)
        
    print("Contact restored successfully")

    return books
