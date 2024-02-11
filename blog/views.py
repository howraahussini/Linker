from typing import Any
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
    
from accounts.models import Account 
from .models import (
    Post,
    Category, 
    Comment
)

from .forms import CommentForm



class PostView(TemplateView):
    '''
    this is for query post list with status == True ,
    '''

    template_name = 'blog/blog.html'
    paginate_by = 5
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.model.objects.filter(status=True)
        context['category'] = Category.objects.all()
        return context
    

class PostSingleView(FormView):
    '''
    this is for single post blog.
    '''

    template_name = 'blog/blog_single.html'
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk = self.kwargs['pk'])
        context["last_post"] = self.model.objects.filter(status=True).order_by("-published_date")[:3]
        context['category'] = Category.objects.all()
        context["comment"] = Comment.objects.filter(post=self.kwargs["pk"], approved=True)
        return context
    
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk = self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "تم الارسال")
        return reverse_lazy("blog:post_single", kwargs={"pk": self.kwargs["pk"]})
    
    
    

class CategorySearch(TemplateView):
    """
    class category filters is for search posts through categories
    """

    template_name = "blog/category_search.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(category__name=self.kwargs["cat"], status=True)
        return context