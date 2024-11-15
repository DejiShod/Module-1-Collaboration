from flask import Flask
app = Flask (__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'


@app.route('/books')
def get_books():
    
    return {"books": "book data"}

from application import app, db

with app.app_context():
    db.create_all()
    
from application import app, db
from application import Book  # Import your model if not already done


books = Book(book_name="48 Laws of Power", author="Robert Greene", publisher="Penguin Random House")


with app.app_context():
    db.session.add(books)
    db.session.commit()
