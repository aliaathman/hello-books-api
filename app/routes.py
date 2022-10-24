from flask import Blueprint, jsonify
hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_response_body = "Hello, World!"
    return my_response_body
@hello_world_bp.route("/hello/JSON", methods=["GET"])
def hello_json():
    return {
        "name": "Alia",
        "message": "Hello!",
        "hobbies": ["Knitting", "Drawing", "Watching Reality Shows"]
    }
@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

class Book:
    def __init__(self,id,title,description):
        self.id = id
        self.title = title
        self.description = description
books = [
    Book(1, "Harry Potter and Sorcerer's Stone", "A fantasy novel set in a imaginary world"),
    Book(2, "Misery", "A horror novel about a writer and a die-hard fan"),
    Book(3, "Book Lovers", "A romance novel about a book editor and a book agent")
    ]
books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods= ["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append(dict(
            id = book.id,
            title = book.title,
            description = book.description
        ))
    return jsonify(books_response)

