# django_app/apps/polls/views.py
from common.caches import get_key_from_cache, set_key_to_cache
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by("-pub_date")
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        cache_key = f"/api/polls/questions/{pk}"
        data = get_key_from_cache(cache_key)

        if data is None:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            set_key_to_cache(cache_key, data, 60 * 30)

        return Response(data)


class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [AllowAny]


class ChoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [AllowAny]
