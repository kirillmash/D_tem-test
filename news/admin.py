from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'user')
    fields = ('title', 'content', 'created_at', 'user')
    search_fields = ('id', 'title')
    readonly_fields = ('created_at',)


admin.site.register(News, NewsAdmin)
