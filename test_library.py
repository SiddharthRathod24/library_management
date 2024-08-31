import unittest
from library import Book, LibraryManager

class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.library_manager = LibraryManager()
        self.book1 = Book("101", "The Art of War", "Sun Tzu")
        self.book2 = Book("102", "1984", "George Orwell")

    def test_add_book(self):
        self.library_manager.add_book(self.book1)
        with self.assertRaises(Exception):
            self.library_manager.add_book(self.book1)  # Adding the same book again

    def test_update_book(self):
        self.library_manager.add_book(self.book1)
        self.library_manager.update_book("101", title="The Art of War - Updated")
        self.assertEqual(self.library_manager.books["101"].title, "The Art of War - Updated")
        with self.assertRaises(Exception):
            self.library_manager.update_book("999", title="Nonexistent")  # Updating a non-existent book

    def test_delete_book(self):
        self.library_manager.add_book(self.book1)
        self.library_manager.delete_book("101")
        with self.assertRaises(Exception):
            self.library_manager.delete_book("101")  # Deleting again should raise an error

    def test_list_books(self):
        self.library_manager.add_book(self.book1)
        self.library_manager.add_book(self.book2)
        books_list = self.library_manager.list_books()
        self.assertIn(self.book1, books_list)
        self.assertIn(self.book2, books_list)

    def test_search_books(self):
        self.library_manager.add_book(self.book1)
        results = self.library_manager.search_books("Art")
        self.assertEqual(len(results), 1)

    def test_check_out_book(self):
        self.library_manager.add_book(self.book1)
        self.library_manager.check_out_book("101")
        with self.assertRaises(Exception):
            self.library_manager.check_out_book("101")  # Should raise an error since it's already checked out

    def test_check_in_book(self):
        self.library_manager.add_book(self.book1)
        self.library_manager.check_out_book("101")
        self.library_manager.check_in_book("101")
        with self.assertRaises(Exception):
            self.library_manager.check_in_book("101")  # Should raise an error since it's already checked in

if __name__ == "__main__":
    unittest.main()