from django.contrib import admin

from APP_BLOG.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
