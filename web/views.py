from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .models import Contact, FAQ
from .forms import ContactForm
from blog.models import Post


class IndexView(TemplateView):
    '''
    this view is for the main page .
    '''

    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_post"] = Post.objects.filter(status=True).order_by("-published_date")[:3]
        return context


class ContactView(FormView):
    '''
    this is for the contact view.
    '''

    template_name = 'web/contact.html'
    form_class = ContactForm
    model = Contact


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faq'] = FAQ.objects.all()
        return context

    def form_valid(self, form):
        self.request.user = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        messages.success(self.request, "تم الارسال")
        return reverse_lazy('web:contact')