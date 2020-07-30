from django.contrib import admin
from .models import Authority, Thread, Message, Topic


admin.site.register(Authority)
admin.site.register(Thread)
admin.site.register(Topic)


class MessageAdmin(admin.ModelAdmin):
    list_filter = ('thread', )
    ordering = ('created_at', )
    exclude = ('indent', )


admin.site.register(Message, MessageAdmin)
