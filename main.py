import sqlite3

connection = sqlite3.connect("library_mego.db")
conn = connection.cursor()
# To create the table.
# conn.execute("create table Books (num_book INTEGER PRIMARY KEY AUTOINCREMENT, name_book text , name_auther text, genre text , language text,"
#              " sum_books integer, location_book text)")
# connection.commit()

# To add a row to the database.
def add_db(name_book, name_auther, genre, language, sum_books, location_book):
    # the command to add.
    conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, sum_books, location_book)"
                 f"VALUES (?,?,?,?,?,?)", (name_book, name_auther, genre, language, sum_books, location_book))
    # save the changes
    connection.commit()

# to show the all database.
def show_all_db(tabel):
    # the command to select all
    conn.execute(f"SELECT * "
                 f"FROM {tabel}")
    # the result.
    rows = conn.fetchall()
    for row in rows:
        print(row)

def show_row_db(tabel,by,typ):
    try:
        # try to pynd the book
        conn.execute(f"SELECT * "
                     f"FROM {tabel} "
                     f"WHERE {by} = ?;", (typ,))
        # the result.
        rows = conn.fetchall()
        for book in rows:
            print(book)
    except:
        print("name error")

# check if is a number
def check_num_book(num):
    return num.isdigit()

def delete(table,by, num_book):

    conn.execute(f"DELETE FROM {table}"
                 f"WHERE {by} = ?;", (num_book,))
    # save the changes.
    connection.commit()
def show_column():
    # to show the column.
    column = conn.execute("PRAGMA table_info(Books)")
    for col in column:
        print(col)


def delete_all(table):
    # to delete all.
    conn.execute(f"DELETE FROM {table}")
    # save the changes.
    connection.commit()

def one_of_the_column(name_column):
    list_name_columns = ["num_book", "name_book", "name_auther", "genre", "language", "sum_books", "location_book"]
    return name_column in list_name_columns

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
        while not check_num_book(sum_books):
            sum_books = input("put in the sum :\n")

        sum_books = int(sum_books)
        add_db(name_book, name_auther, genre, language, sum_books, location_book)
        print("the book is added")
    elif to_do == "del":
        show_column()
        by = "num_book"
        book = input("chose the num of the book\n")

    elif to_do == "show":
        show_all_db("Books")
    elif to_do == "search":
        by = (input("search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        while not one_of_the_column(by):
            by = (input(
                "search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        book = input("the mark of the book\n")
        show_row_db("Books",by,book)
    elif to_do != "exit":
        print("chose one of de option")
conn.close()
connection.close()

# Test comment