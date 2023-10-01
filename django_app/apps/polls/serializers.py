# django_app/apps/polls/serializers.py
from rest_framework import serializers

from .models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "question", "choice_text", "votes")


class ChoiceInsideQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "choice_text", "votes")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceInsideQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "choices")
