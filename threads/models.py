from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Authority(models.Model):

    class Meta:
        verbose_name_plural = "Authorities"

    name = models.CharField(max_length=64)
    photo = models.ImageField(null=True, blank=True, upload_to='uploads/photos/')
    description = models.TextField(null=True, blank=True)
    is_deputy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Thread(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    author = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    previous = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='answers')
    attachment = models.FileField(null=True, blank=True, upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    indent = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.author.name + ": " + self.text[:100]


@receiver(pre_save, sender=Message)
def add_indent(sender, instance, *args, **kwargs):
    if instance.previous is None:
        instance.indent = 0
    else:
        instance.indent = instance.previous.indent + 1