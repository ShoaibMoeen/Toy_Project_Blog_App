from django.test import TestCase
from users.models import Writer

class userTests(TestCase):

    def test_new_writer_status_verification(self):
        test_user= Writer(name="TestUser", username="TU123", email="TU@gmail.com")
        self.assertIs(test_user.is_editor, False)