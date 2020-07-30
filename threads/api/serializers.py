from rest_framework import serializers
from threads.models import Thread, Topic, Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        exclude = ["created_at", "modified_at"]

    author_name = serializers.SerializerMethodField(read_only=True)
    author_photo = serializers.SerializerMethodField(read_only=True)
    thread_title = serializers.SerializerMethodField(read_only=True)
    indent = serializers.IntegerField(read_only=True)

    @staticmethod
    def get_author_name(instance):
        return instance.author.name

    @staticmethod
    def get_author_photo(instance):
        if instance.author.photo:
            return instance.author.photo.url
        return '/media/nophoto.jpg'

    @staticmethod
    def get_thread_title(instance):
        return instance.thread.title


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = "__all__"

    messages = MessageSerializer(many=True, required=False)


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
