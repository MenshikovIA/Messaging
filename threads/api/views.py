from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from threads.api.pagination import ThreadPaginator
from threads.api.serializers import ThreadSerializer, MessageSerializer, TopicSerializer
from threads.models import Topic, Thread, Message


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all().order_by('-created_at')
    serializer_class = ThreadSerializer
    pagination_class = ThreadPaginator


class TopicViewSet(generics.ListAPIView):
    serializer_class = ThreadSerializer
    pagination_class = ThreadPaginator

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Thread.objects.filter(topic_id=pk).order_by("-created_at")


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
