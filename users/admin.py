from django.contrib import admin
from .models import CustomUser, Comment, Post

admin.register(CustomUser)
admin.register(Comment)
admin.register(Post)
