from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
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
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author, 'publisher' : book.publisher}
        
        output.append(book_data)
    
    return {"books": output}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # Check if the book already exists
        existing_book = Book.query.filter_by(book_name="48 Laws of Power").first()
        if not existing_book:
            new_book = Book(
                book_name="48 Laws of Power",
                author="Robert Greene",
                publisher="Penguin Random House"
            )
            db.session.add(new_book)
            db.session.commit()
        else:
            print(f"Book '{existing_book.book_name}' already exists in the database.")

    # Run the app
    app.run(debug=True)