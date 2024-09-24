from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at') 
    search_fields = ('title', 'created_at') 
    list_filter = ['created_at']
    ordering = ('-created_at',) 
    
admin.site.register(Post, PostAdmin)