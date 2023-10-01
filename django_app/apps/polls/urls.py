# django_app/apps/polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("questions/", views.QuestionListCreateView.as_view(), name="question-list-create"),
    path("questions/<int:pk>/", views.QuestionRetrieveUpdateDestroyView.as_view(), name="question-detail"),
    path("choices/", views.ChoiceListCreateView.as_view(), name="choice-list-create"),
    path("choices/<int:pk>/", views.ChoiceRetrieveUpdateDestroyView.as_view(), name="choice-detail"),
]
