import Class_db
db = Class_db.Class_db()


to_do = ""
while to_do != "exit":
    to_do = input("input what you want to do \nto add a book (add)\nto delete a book (del)\nto show all row (show)\n"
                  "to search a book (search)\n")
    if to_do == "add":
        flag = True
        while flag is True:
            try:
                name_book, name_auther, genre, language, sum_books, location_book = input("put in the all information by the order"
                                                                                  "with a separator (,)\n"
                                                                                  "(name_book, name_auther, genre, language, sum_books, location_book)\n").split(",")
                flag = False
            except:
                print("put in the coract book by the column")
        while not sum_books.isdigit():
            sum_books = input("put in the sum :\n")

        sum_books = int(sum_books)
        db.add_book(name_book, name_auther, genre, language, sum_books, location_book)
        print("the book is added")
    elif to_do == "del":
        db.show_columns_data()
        by = "num_book"
        book = input("chose the num of the book\n")

    elif to_do == "show":
        db.show_entire_table("Books")
    elif to_do == "search":
        by = (input("search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        while not db.is_valid_column(by):
            by = (input(
                "search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        book = input("the mark of the book\n")
        db.show_single_row("Books", by, book)
    elif to_do != "exit":
        print("chose one of de option")

