import unittest
from unittest.mock import Mock
from services.reference_services import ReferenceService
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.mock_reference_repository = Mock()
        self.reference_service = ReferenceService(self.mock_reference_repository)

    def test_create_reference_book(self):
        fields = ['Author Name', 'Book Title', '2023', 'Publisher Name', '']
        self.reference_service.create_reference('book', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, Book)
        self.assertEqual(new_ref.author, 'Author Name')

    def test_create_reference_article(self):
        fields = ['Author Name', 'Article Title', 'Journal', '2023', '']
        self.reference_service.create_reference('article', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, Article)
        self.assertEqual(new_ref.author, 'Author Name')

    def test_create_reference_inproceedings(self):
        fields = ['Author Name', 'Title', 'Book Title', 'Publisher Name', '2023', '']
        self.reference_service.create_reference('inproceedings', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, InProceedings)
        self.assertEqual(new_ref.author, 'Author Name')

    # Copy similar to other types
    # Also need to test for faulty input "refence type = foobar"

