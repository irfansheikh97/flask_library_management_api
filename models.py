books = []
members = []

class Book:
    id_counter = 1

    def __init__(self, title: str, author: str, copies: int):
        self.id = Book.id_counter
        self.title = title
        self.author = author
        self.copies = copies
        Book.id_counter += 1

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'copies': self.copies}


class Member:
    id_counter = 1

    def __init__(self, name: str, email: str):
        self.id = Member.id_counter
        self.name = name
        self.email = email
        Member.id_counter += 1

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
