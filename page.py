from flask import Flask, render_template

app = Flask(__name__)
<<<<<<< HEAD
# the first page.
@app.route("/")
def index():
    # return the html page.
    return render_template('index.html')
#  turn on the website.
=======

@app.route("/")
def index():
    return render_template('index.html')

>>>>>>> origin/Development
if __name__ == '__main__':
    app.run(debug=True)