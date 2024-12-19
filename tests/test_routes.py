import unittest
from app import app
from models import books, Book

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        books.clear()
        self.book1 = Book("Dreams", "Sam Alter", 5)
        self.book2 = Book("Dreams and Reality", "Sam Holland", 3)
        books.extend([self.book1, self.book2])

    def test_add_book(self):
        new_book = {"title": "New Book", "author": "New Author", "copies": 10}
        response = self.app.post('/books/', json=new_book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "New Book")

    def test_get_books(self):
        response = self.app.get('/books/')
        print(response.json)  # Debugging output
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)  # Expect 2 books
        self.assertIn(self.book1.to_dict(), response.json)
        self.assertIn(self.book2.to_dict(), response.json)

    def test_update_book(self):
        update_data = {"title": "Updated Title"}
        print([book.to_dict() for book in books])  # Debugging: Print books before the update
        response = self.app.put(f'/books/{self.book1.id}', json=update_data)
        self.assertEqual(response.status_code, 200)

        # Verify the book was updated
        updated_book = next(b for b in books if b.id == self.book1.id)
        self.assertEqual(updated_book.title, "Updated Title")

    def test_delete_book(self):
        response = self.app.delete(f'/books/{self.book1.id}')
        self.assertEqual(response.status_code, 200)
        # Verify book count after deletion
        response = self.app.get('/books/')
        self.assertEqual(len(response.json), 1)
        self.assertNotIn(self.book1.to_dict(), response.json)


    def test_pagination(self):
        response = self.app.get('/books/?page=1&limit=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
