from rest_framework.pagination import PageNumberPagination


class ThreadPaginator(PageNumberPagination):
    page_size = 5
