import sqlite3
class Class_db:
    def __init__(self):
        self.connection = sqlite3.connect("library_mego.db")
        self.conn = self.connection.cursor()

    # To add a row to the database.
    def add_book(self, tuple_arg):
        # the command to add.
        self.conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, sum_books, location_book)"
                        f"VALUES (?,?,?,?,?,?)", tuple_arg)
        # save the changes
        self.connection.commit()

    # to show the all database.
    def show_entire_table(self, table_name):
        # the command to select all
        self.conn.execute(f"SELECT * "
                     f"FROM {table_name}")
        # the result.
        rows = self.conn.fetchall()
        for row in rows:
            print(row)

    def show_single_row(self, table_name, filter_by, filter_value):
        try:
            # try to pynd the book
            self.conn.execute(f"SELECT * "
                         f"FROM {table_name} "
                         f"WHERE {filter_by} = ?;", (filter_value,))
            # the result.
            rows = self.conn.fetchall()
            for book in rows:
                print(book)
        except:
            print("name error")

    # to delete a book.
    def delete_book(self, table_name, filter_by, filter_value):

        self.conn.execute(f"DELETE FROM {table_name}"
                     f"WHERE {filter_by} = ?;", (filter_value,))
        # save the changes.
        self.connection.commit()

    def show_columns_data(self):
        # to show the column.
        columns = self.conn.execute("PRAGMA table_info(Books)")
        for col in columns:
            print(col)


    def delete_all_books(self, table_name):
        # to delete all.
        self.conn.execute(f"DELETE FROM {table_name}")
        # save the changes.
        self.connection.commit()

    def is_valid_column(self, column_name):
        column_names = ["num_book", "name_book", "name_auther", "genre", "language", "sum_books", "location_book"]
        return column_name in column_names

    # to closs the database
    def clos_the_db(self):
        self.conn.close()
        self.connection.close()