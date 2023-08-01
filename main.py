import sqlite3

connection = sqlite3.connect("library_mego.db")
conn = connection.cursor()
# To create the table.
# conn.execute("create table Books (num_book INTEGER PRIMARY KEY AUTOINCREMENT, name_book text , name_auther text, genre text , language text,"
#              " sum_books integer, location_book text)")
# connection.commit()

# To add a row to the database.
def add_book(name_book, name_auther, genre, language, sum_books, location_book):
    # the command to add.
    conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, sum_books, location_book)"
                 f"VALUES (?,?,?,?,?,?)", (name_book, name_auther, genre, language, sum_books, location_book))
    # save the changes
    connection.commit()

# to show the all database.
def show_entire_table(table_name):
    # the command to select all
    conn.execute(f"SELECT * "
                 f"FROM {table_name}")
    # the result.
    rows = conn.fetchall()
    for row in rows:
        print(row)

def show_single_row(table_name, filter_by, filter_value):
    try:
        # try to pynd the book
        conn.execute(f"SELECT * "
                     f"FROM {table_name} "
                     f"WHERE {filter_by} = ?;", (filter_value,))
        # the result.
        rows = conn.fetchall()
        for book in rows:
            print(book)
    except:
        print("name error")

# check if it's a number
def is_number(num):
    return num.isdigit()

def delete_book(table_name, filter_by, filter_value):

    conn.execute(f"DELETE FROM {table_name}"
                 f"WHERE {filter_by} = ?;", (filter_value,))
    # save the changes.
    connection.commit()
def show_columns_data():
    # to show the column.
    columns = conn.execute("PRAGMA table_info(Books)")
    for col in columns:
        print(col)


def delete_all_books(table_name):
    # to delete all.
    conn.execute(f"DELETE FROM {table_name}")
    # save the changes.
    connection.commit()

def is_valid_column(column_name):
    column_names = ["num_book", "name_book", "name_auther", "genre", "language", "sum_books", "location_book"]
    return column_name in column_names

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
        while not is_number(sum_books):
            sum_books = input("put in the sum :\n")

        sum_books = int(sum_books)
        add_book(name_book, name_auther, genre, language, sum_books, location_book)
        print("the book is added")
    elif to_do == "del":
        show_columns_data()
        by = "num_book"
        book = input("chose the num of the book\n")

    elif to_do == "show":
        show_entire_table("Books")
    elif to_do == "search":
        by = (input("search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        while not is_valid_column(by):
            by = (input(
                "search by 1 of the option (num_book, name_book, name_auther, genre, language, sum_books, location_book)\n"))
        book = input("the mark of the book\n")
        show_single_row("Books", by, book)
    elif to_do != "exit":
        print("chose one of de option")
conn.close()
connection.close()

# Test comment