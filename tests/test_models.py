import unittest
from models import Book, Member

class TestModels(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Test Title", "Test Author", 5)
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.copies, 5)

    def test_member_creation(self):
        member = Member("Test Name", "test@example.com")
        self.assertEqual(member.name, "Test Name")
        self.assertEqual(member.email, "test@example.com")
