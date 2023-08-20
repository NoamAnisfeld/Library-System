from flask import Flask, redirect, url_for, render_template, request, flash
import Class_db
app = Flask(__name__)
# to use the database.

db = Class_db.Class_db()
# the first page.
@app.route("/", methods=["POST","GET"])
def index():
    # check if the html send the information or not.
    if request.method == "POST":
        # return the function add_book.
        return redirect(url_for("add_book"))
    else:
        return render_template('library.html')
@app.route("/add_book", methods=["POST","GET"])
def add_book():
    # check if the html send the information or not.
    if request.method == "POST":
        # pot a dictionary in user.
        user = request.form
        # check if it's a number.
        if not user["sum_books"].isdigit():
            return render_template("add_books_page.html")
        for i in user:
            print(user[i])
        user = tuple(user.values())
        # add the book to the database
        db.add_book(user)
        print(user)
        # return the function book_adds that show the book.
        return redirect(url_for("book_adds", book=user))
    else:
        return render_template("add_books_page.html")

@app.route("/<book>")
def book_adds(book):
    return f"<h1>{book}</h1>"
#  turn on the website.
if __name__ == '__main__':
    app.run()

