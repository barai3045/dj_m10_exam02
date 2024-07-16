def save_books(books):
    with open("books.csv", "w") as fp:
        for book in books:
            line = f"{book['title']},{book['authors']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)


def save_lents(lent_books):
    with open("lents.csv", "w") as fp:
        for lent_book in lent_books:
            line = f"{lent_book['title']},{lent_book['borrower']},{lent_book['isbn']}\n"
            fp.write(line)


def restore_books(books):
    # open file 
    # read all contacts 
    # save them to global contact book variable
    try: 
        books.clear()
        with open("books.csv", "r") as fp:
            # print(type(fp.read()))
            for line in fp.readlines():
                line_splitted = line.strip().split(",")
                
                book = {
                    "title": line_splitted[0],
                    "authors": line_splitted[1],
                    "isbn": line_splitted[2],
                    "year": line_splitted[3],
                    "price": line_splitted[4],
                    "quantity": line_splitted[5]
                }
                
                books.append(book)
        print("Books restored successfully")
    except(FileNotFoundError, ValueError):
        print("There are some error")

def restore_books_lend(books):
    try:
        books.clear()
        with open("books_lent.csv", "r") as fp:
            for line in fp.readlines():
                line_splitted = line.strip().split(",")
                lent_book = {
                    "title": line_splitted[0],
                    "borrower": line_splitted[1],
                    "isbn": line_splitted[2],
                }
                books.append(lent_book)
  
    except (FileNotFoundError, ValueError):
        print("There are some error")