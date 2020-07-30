from django.shortcuts import render
from django.views import View

from django.conf import settings


class IndexView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        if settings.DEBUG:
            template = 'threads/index-dev.html'
        else:
            template = 'threads/index.html'
        return render(request, template)
