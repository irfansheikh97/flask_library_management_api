from flask import Blueprint, request, jsonify
from models import books, members, Book, Member

book_routes = Blueprint('books', __name__)
member_routes = Blueprint('members', __name__)
search = Blueprint('search', __name__)

# CRUD for Books
@book_routes.route('/', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    
    filtered_books = books
    if title:
        filtered_books = [b for b in books if title.lower() in b.title.lower()]
    if author:
        filtered_books = [b for b in filtered_books if author.lower() in b.author.lower()]
    
    start = (page - 1) * limit
    end = start + limit
    return jsonify([b.to_dict() for b in filtered_books[start:end]])

@book_routes.route('/', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], copies=data['copies'])
    books.append(new_book)
    return jsonify(new_book.to_dict()), 201

@book_routes.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.copies = data.get('copies', book.copies)
    return jsonify(book.to_dict())

@book_routes.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b.id != book_id]
    return jsonify({'message': 'Book deleted'})

# CRUD for Members
@member_routes.route('/', methods=['GET'])
def get_members():
    return jsonify([m.to_dict() for m in members])

@member_routes.route('/', methods=['POST'])
def add_member():
    data = request.json
    new_member = Member(name=data['name'], email=data['email'])
    members.append(new_member)
    return jsonify(new_member.to_dict()), 201

@member_routes.route('/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = next((m for m in members if m.id == member_id), None)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    return jsonify(member.to_dict())

@member_routes.route('/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [m for m in members if m.id != member_id]
    return jsonify({'message': 'Member deleted'})


@search.route('/', methods=['GET'])
def search_books():
    title_query = request.args.get('title', '').strip().lower()
    author_query = request.args.get('author', '').strip().lower()
    page = int(request.args.get('page', 1))  # Default page is 1
    limit = int(request.args.get('limit', 5))  # Default limit is 5

    # Ensure at least one query parameter is provided
    if not title_query and not author_query:
        return jsonify({'message': 'No title or author query provided.'}), 400

    # Filter books based on title or author
    results = [
        book.to_dict() for book in books
        if (title_query and title_query in book.title.lower())
        or (author_query and author_query in book.author.lower())
    ]

    # Paginate results
    total_results = len(results)
    start = (page - 1) * limit
    end = start + limit
    paginated_results = results[start:end]

    # Check if results are empty
    if not paginated_results:
        return jsonify({'message': 'No books found for the given query on this page.'}), 404

    # Response with pagination metadata
    response = {
        "total_results": total_results,
        "page": page,
        "limit": limit,
        "results": paginated_results
    }
    return jsonify(response), 200



