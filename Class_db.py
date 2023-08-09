import sqlite3
class Class_db:

    # To add a row to the database.
    def add_book(self, tuple_arg):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # the command to add.
        conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, sum_books, location_book)"
                          f"VALUES (?,?,?,?,?,?)", tuple_arg)
        # save the changes
        connection.commit()
        # close the conaction.
        conn.close()
        connection.close()


    # to show the all database.
    def show_entire_table(self, table_name):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # the command to select all
        conn.execute(f"SELECT * "
                     f"FROM {table_name}")
        # the result.
        rows = conn.fetchall()
        for row in rows:
            print(row)
        # close the conaction.
        conn.close()
        connection.close()

    def show_single_row(self, table_name, filter_by, filter_value):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
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
        # close the conaction.
        conn.close()
        connection.close()


    # to delete a book.
    def delete_book(self, table_name, filter_by, filter_value):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        conn.execute(f"DELETE FROM {table_name}"
                     f"WHERE {filter_by} = ?;", (filter_value,))
        # save the changes.
        connection.commit()
        # close the conaction.
        conn.close()
        connection.close()

    def show_columns_data(self):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # to show the column.
        columns = conn.execute("PRAGMA table_info(Books)")
        for col in columns:
            print(col)
        # close the conaction.
        conn.close()
        connection.close()

    def delete_all_books(self, table_name):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # to delete all.
        conn.execute(f"DELETE FROM {table_name}")
        # save the changes.
        connection.commit()
        # close the conaction.
        conn.close()
        connection.close()

    def is_valid_column(self, column_name):
        column_names = ["num_book", "name_book", "name_auther", "genre", "language", "sum_books", "location_book"]
        return column_name in column_names
