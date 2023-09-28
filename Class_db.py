import sqlite3


# to create and delete the database to use only one's
####################################################################################
def create_tabel():
    connection = sqlite3.connect("library_mego.db")
    conn = connection.cursor()
    conn.execute(f"CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, name_book TEXT, name_auther TEXT, genre TEXT, language TEXT, location_book TEXT,accompanied text);")
    # save the changes
    connection.commit()
    # close the conaction.
    conn.close()
    connection.close()

def delete_dable(table):

    connection = sqlite3.connect("library_mego.db")
    conn = connection.cursor()
    conn.execute(f"DROP TABLE {table};")
    # save the changes
    connection.commit()
    # close the conaction.
    conn.close()
    connection.close()

####################################################################

class Class_db:

    # To add a row to the database.
    def add_book(self, tuple_arg):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # the command to add.
        conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, location_book,accompanied)"
                          f"VALUES (?,?,?,?,?,?)", tuple_arg)
        # save the changes
        connection.commit()
        # close the conaction.
        conn.close()
        connection.close()

    def change_a_column_in_a_row(self, table_name, column_name, new_value, id):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        # the command to change.
        conn.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?",(new_value, id) )
        # get bake if is seccs.
        if conn.rowcount > 0:
            # save the changes
            connection.commit()
            # close the conaction.
            conn.close()
            connection.close()
            return True
        # close the conaction.
        conn.close()
        connection.close()
        return False


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
        # close the conaction.
        conn.close()
        connection.close()
        return rows

    def show_single_row(self, table_name, filter_by, filter_value):
        # open the conaction.
        connection = sqlite3.connect("library_mego.db")
        conn = connection.cursor()
        rows = []
        try:

            # try to pynd the book
            conn.execute(f"SELECT * "
                         f"FROM {table_name} "
                         f"WHERE {filter_by} = ?;", (filter_value,))
            # the result.
            rows = conn.fetchall()
        except:
            print("name error")
        # close the conaction.
        conn.close()
        connection.close()
        return rows



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
        
        # close the conaction.
        conn.close()
        connection.close()
        return columns

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
        column_names = ["num_book", "name_book", "name_auther", "genre", "language","accompanied" , "location_book"]
        return column_name in column_names



#  plaay only whan the page is running.
if __name__ == "__main__":
    # to delete the table
    # delete_dable("books)
    # to create the table
    # create_tabel()
    db = Class_db()
    db.add_book((("namevecrvfcw", "name_autvdvfvfdher"," genrvrefwcere","languecdcdsage", "location_book","True")))
    for item in db.show_entire_table("books"):
        print(item)
