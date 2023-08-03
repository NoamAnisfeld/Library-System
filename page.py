from flask import Flask, redirect, url_for, render_template, request, flash
import main
app = Flask(__name__)

# the first page.
@app.route("/", methods=["POST","GET"])
def index():
    # return the html page.
    if request.method == "POST":
        return redirect(url_for("add_book"))
    else:
        return render_template('index.html')
@app.route("/add_book", methods=["POST","GET"])
def add_book():
    if request.method == "POST":
        user = request.form
        if not user["sum_books"].isdigit():
            # flash("it need to be a number")
            return render_template("add_books_page.html")
        for i in user:
            print(user[i])
        user = tuple(user.values())
        main.add_book(user)
        print(user)
        return redirect(url_for("book_adds", book=user))

    else:
        return render_template("add_books_page.html")

@app.route("/<book>")
def book_adds(book):
    return f"<h1>{book}</h1>"
#  turn on the website.
if __name__ == '__main__':
    app.run(debug=True)