
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'



@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}
        
        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return{"name":book.name, "description":book.description}

@app.route('/publishers')
def get_publishers():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}
        
        output.append(book_data)

    return {"books": output}


@app.route('/authors')
def get_authors():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}
        
        output.append(book_data)

    return {"books": output}

