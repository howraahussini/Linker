from typing import Any
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView, DeleteView
from django.urls import reverse_lazy
from itertools import chain

from accounts.models import Account
from .models import MainLink
from .forms import MainLinkForm
from panel.models import (
    Profile,
    Text,
    Link,
    Gallery,
    FAQUser
)
from social_media.models import (
    Email,
    Phone,
    Instagram,
    Telegram,
    Youtube,
    Whatsapp,
    X,
    Facebook,
    Linkedin,
    Snapchat,
    Tiktok
)


class CommonContextMixin:
    '''
    This is for the maine link page and displaying everything user made and sort item by created_date.
    '''

    # model = MainLink

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # this is for send kwargs link_name with url
        link_name = self.kwargs['link_name']
        main_link = MainLink.objects.get(name=link_name)
        context['link_name'] = main_link

        # this is for check user to be the owner or not
        context['page_owner_email'] = main_link.author.user.email 


        # Profile
        context['profile'] = Profile.objects.get(link_id__name = link_name)


        all_models = list(chain(

            # Text
            Text.objects.filter(link_id__name=link_name),
            

            # Link
            Link.objects.filter(link_id__name=link_name),
            

            # Gallery
            Gallery.objects.filter(link_id__name=link_name),
        

            # FAQUsers
            FAQUser.objects.filter(link_id__name = link_name),


            # Email
            Email.objects.filter(link_id__name = link_name),
       

            # Phone
            Phone.objects.filter(link_id__name = link_name),


            # Instagram
            Instagram.objects.filter(link_id__name = link_name),
            

            # Telegram
            Telegram.objects.filter(link_id__name = link_name),


            # Youtube
            Youtube.objects.filter(link_id__name = link_name),

        
            # Whatsapp
            Whatsapp.objects.filter(link_id__name = link_name),


            # Facebook
            Facebook.objects.filter(link_id__name = link_name),


            # X
            X.objects.filter(link_id__name = link_name),


            # Linkedin
            Linkedin.objects.filter(link_id__name = link_name),


            # Snapchat
            Snapchat.objects.filter(link_id__name = link_name),


            # Tiktok
            Tiktok.objects.filter(link_id__name = link_name)
        
        ))


        # this context contain all models for show in the template and sorted all item by created_date 
        context['all_models'] = all_models
    
        return context

    


class MainLinkView(CommonContextMixin, TemplateView):
    '''
    This is for the maine link page and displaying everything user made .
    '''

    template_name = 'dashboard/main_link.html'
    model = MainLink

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    '''
    this is for displaying a MainLinkForm and a the list of links that the user made.
    '''

    template_name = 'dashboard/dashboard.html'
    model = MainLink
    form_class = MainLinkForm 
    ordering = 'created_date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.filter(link_id__author__user = self.request.user)

        context['form'] = self.form_class
        return context
    

    def form_valid(self, form):
        form.instance.author = Account.objects.get(user = self.request.user)
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, "تم اضافة الرابط")
        return reverse_lazy('dashboard:dashboard')
    
    def test_func(self):
        return self.request.user.id == self.request.user.id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))
    

class MainLinkDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    this is for delete main link in dashboard page.
    '''

    template_name = 'dashboard/dashboard.html'
    model = MainLink

    def get_success_url(self):
        messages.success(self.request, "تم الحذف")
        return reverse_lazy('dashboard:dashboard')
    
    def test_func(self):
        main_link = self.get_object() 
        return self.request.user.id == main_link.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))
    
