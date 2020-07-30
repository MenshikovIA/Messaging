from django.urls import path, include
from rest_framework.routers import DefaultRouter

from threads.api import views as tv
from threads.api.views import TopicViewSet, TopicList


router = DefaultRouter()
router.register(r"threads", tv.ThreadViewSet)
router.register(r"messages", tv.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('topic/<int:pk>/', TopicViewSet.as_view()),
    path('topics/', TopicList.as_view()),
]
