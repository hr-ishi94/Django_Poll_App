from django.test import TestCase
import datetime
from .models import Question
from django.utils import timezone

# Create your tests here.


class QuestionModeTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() function must returns false for questions in the future
        """
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = future_date)
        self.assertIs(future_question.was_published_recently(),False)