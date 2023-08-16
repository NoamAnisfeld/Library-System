from flask import Flask, render_template

app = Flask(__name__)
# the first page.
@app.route("/")
def index():
    # return the html page.
    return render_template('library.html')
#  turn on the website.
if __name__ == '__main__':
    app.run(debug=True)