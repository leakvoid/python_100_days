from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    global all_books
    return render_template('index.html', all_books=all_books, length=len(all_books))


@app.route("/add", methods=['GET', 'POST'])
def add():
    global all_books
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        all_books.append(data)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port=6300)