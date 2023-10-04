from flask import Flask, redirect, url_for, render_template, request, flash
import Class_db

app = Flask(__name__)
# to use the database.


db = Class_db.Class_db()


# the first page.
@app.route("/")
def index():
    return render_template('library.html')


@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    # check if the html send the information or not.
    if request.method == "POST":
        # put a dictionary in user.
        user = request.form
        user = tuple(user.values())
        # add the book to the database
        db.add_book(user)
        # return the function book_adds that show the book.
        return redirect(url_for("show_books"))
    else:
        return render_template("add_books_page.html")


@app.route("/show_books")
def show_books():
    information = db.show_entire_table("books")
    return render_template("show db.html", information=information)


@app.route("/search_book", methods=['POST', 'GET'])
# route search button and search field
def search_book():
    # route search field
    if request.method == 'POST':
        #  get the row of the relevant book from DB
        information = db.show_single_row('books', 'name_book', request.form['search-field'])
        return render_template("show db.html", information=information)

    else:
        # route the search button
        return render_template('search_book.html')


#  turn on the website.
if __name__ == '__main__':
    app.run(debug=True)
