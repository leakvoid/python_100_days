from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>This is a paragraph</p>'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello, {name}, the number is {number}!"

def make_bold(func):
    def wrapper():
        return func()
    return wrapper

def make_emphasis(func):
    def wrapper():
        return func()
    return wrapper

def make_underlined(func):
    def wrapper():
        return func()
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True) # enable debug mode