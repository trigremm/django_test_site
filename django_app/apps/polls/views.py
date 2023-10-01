# django_app/apps/polls/views.py
from rest_framework import generics

from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by("-pub_date")
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
