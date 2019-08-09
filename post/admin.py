from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    field = ('title', 'content', 'created')


admin.site.register(Post, PostAdmin)
