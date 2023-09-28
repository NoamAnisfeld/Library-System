from flask import Flask, redirect, url_for, render_template, request, flash , jsonify
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

@app.route("/take_book",methods=['POST', 'GET'])
def take_book():
    information = db.show_entire_table("books")
    print(information)
    if request.method == 'POST':
        index_book_take = int(request.form['data'])
        id_of_the_book = information[index_book_take][0]
        change_the_db = db.change_a_column_in_a_row("books","accompanied","False",id_of_the_book)
        print(change_the_db)
        # return the function book_adds that show the book.
        if change_the_db:
            return jsonify({"data": "true","id":id_of_the_book,"index":information[index_book_take]})
        else:
            return jsonify({"data": "false"})

    else:
        return render_template("take_book.html", books=information)


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
