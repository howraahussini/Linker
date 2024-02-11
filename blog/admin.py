from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    '''
    this is for managing posts.
    '''

    model = Post
    list_display = ('title', 'category', 'status', 'author', 'created_date', 'updated_date')
    search_fields = ('title', 'content', 'category')
    list_filter = ('category', 'status', 'author', 'created_date')


class CategoryAdmin(admin.ModelAdmin):
    '''
    this is for managing category.
    '''

    model = Category
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class CommentAdmin(admin.ModelAdmin):
    """
    this is for the comment model management
    """

    model = Comment
    list_filter = ("created_date", "approved", "post")
    list_display = ("name", "post", "approved", "created_date")
    search_fields = ("name", "post", "subject", "message")
    ordering = ("created_date",)


admin.site.register(Post, PostAdmin)    
admin.site.register(Category, CategoryAdmin)    
admin.site.register(Comment, CommentAdmin)    