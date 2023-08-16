from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# the first page.
@app.route("/")
def index():

    connection = sqlite3.connect("library_mego.db")
    conn = connection.cursor()
    # the command to add.
    conn.execute(f"INSERT INTO books (name_book, name_auther, genre, language, sum_books, location_book)"
                 f"VALUES (?,?,?,?,?,?)", ('Harry Potter', 'J.K. Rowling', 'Fantasy', 'English', 2, 'somewhere'))
    # save the changes
    connection.commit()
    # close the conaction.
    conn.close()
    connection.close()

    connection = sqlite3.connect("library_mego.db")
    conn = connection.cursor()

    conn.execute(f"SELECT * "
                 f"FROM books")
    # the result.
    rows = conn.fetchall()
    result = ''
    for row in rows:
        result = result + str(row)

    conn.close()
    connection.close()

    # return the html page.
    return result
#  turn on the website.
if __name__ == '__main__':
    app.run(debug=True)