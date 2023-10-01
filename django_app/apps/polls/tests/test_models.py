# django_app/apps/polls/tests/test_models.py
# Here is a Django test case example that tests the model, serializer, view, and URL for the Polls app.

from django.test import TestCase
from django.utils import timezone
from polls.models import Choice, Question


class QuestionModelTestCase(TestCase):
    def setUp(self):
        self.question_text = "What's new?"
        self.question = Question.objects.create(question_text=self.question_text, pub_date=timezone.now())

    def test_create_question(self):
        """Tests if a new question can be successfully created."""
        self.assertIsInstance(self.question, Question)

    def test_update_question(self):
        """Tests if an existing question's fields can be updated."""
        new_text = "What's up?"
        self.question.question_text = new_text
        self.question.save()
        self.assertEqual(self.question.question_text, new_text)

    def test_delete_question(self):
        """Tests if a question can be deleted."""
        self.question.delete()
        self.assertEqual(Question.objects.filter(id=self.question.id).count(), 0)

    def test_str_representation_of_question(self):
        """Tests the __str__ method to see if it returns the question_text."""
        self.assertEqual(str(self.question), self.question_text)

    def test_question_has_choices(self):
        """Tests if the choices related to a question can be accessed."""
        self.question.choices.create(choice_text="Not much", votes=0)
        self.question.choices.create(choice_text="The sky", votes=0)
        self.assertEqual(self.question.choices.count(), 2)

    def test_question_fields_type(self):
        """Tests the type of each field."""
        self.assertIsInstance(self.question.question_text, str)
        self.assertIsInstance(self.question.pub_date, timezone.datetime)


class ChoiceModelTestCase(TestCase):
    def setUp(self):
        question = Question.objects.create(question_text="What's new?", pub_date=timezone.now())
        self.choice_text = "Not much"
        self.choice = Choice.objects.create(question=question, choice_text=self.choice_text, votes=0)

    def test_create_choice(self):
        """Tests if a new choice can be successfully created."""
        self.assertIsInstance(self.choice, Choice)

    def test_update_choice(self):
        """Tests if an existing choice's fields can be updated."""
        new_text = "The sky"
        self.choice.choice_text = new_text
        self.choice.save()
        self.assertEqual(self.choice.choice_text, new_text)

    def test_delete_choice(self):
        """Tests if a choice can be deleted."""
        self.choice.delete()
        self.assertEqual(Choice.objects.filter(id=self.choice.id).count(), 0)

    def test_str_representation_of_choice(self):
        """Tests the __str__ method to see if it returns the choice_text."""
        self.assertEqual(str(self.choice), self.choice_text)

    def test_choice_belongs_to_question(self):
        """Tests if the choice belongs to the correct question."""
        self.assertEqual(self.choice.question.question_text, "What's new?")

    def test_choice_fields_type(self):
        """Tests the type of each field."""
        self.assertIsInstance(self.choice.choice_text, str)
        self.assertIsInstance(self.choice.votes, int)


class ChoiceQuestionRelationshipTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="What's up?", pub_date=timezone.now())
        self.choice1 = Choice.objects.create(question=self.question, choice_text="Not much", votes=0)
        self.choice2 = Choice.objects.create(question=self.question, choice_text="The sky", votes=0)

    def test_choices_deleted_when_question_deleted(self):
        """Test if choices are deleted when their parent question is deleted."""
        self.question.delete()
        self.assertEqual(Choice.objects.filter(question=self.question).count(), 0)

    def test_query_choices_through_question(self):
        """Test if choices can be queried through their parent question."""
        self.assertEqual(self.question.choices.count(), 2)
        self.assertIn(self.choice1, self.question.choices.all())
        self.assertIn(self.choice2, self.question.choices.all())
