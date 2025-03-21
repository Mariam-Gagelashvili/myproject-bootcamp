from django.contrib import admin
from .models import Post
from .models import Product
from .models import Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Comment)