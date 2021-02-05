from django.test import TestCase
from article.models import Article
from datetime import date


class articleTests(TestCase):

    def test_new_article_status_verification(self):
        test_article = Article(title='Beatles Blog', content='All the latest Beatles news.')
        self.assertIs(test_article.status, 'pending')

    def test_new_article_creation_time(self):
        test_article = Article(title='The Weeknd', content='Starboy')
        self.assertIs(test_article.edited_by, None)    