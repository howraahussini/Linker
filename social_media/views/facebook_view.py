from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    FormView,
    UpdateView,
    DeleteView
)

from dashboard.views import CommonContextMixin
from accounts.models import Account
from dashboard.models import MainLink
from ..models import Facebook
from ..forms import FacebookForm



class FacebookView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, FormView):
    '''
    this is for displaying Facebook form in the template.
    '''

    template_name = 'social_media/Facebook/Facebook.html'
    model = Facebook
    form_class = FacebookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def form_valid(self, form):
        form.instance.link_id = MainLink.objects.get(name = self.kwargs['link_name'])
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('panel:modules_page', kwargs={'link_name': self.kwargs['link_name']})
    
    def test_func(self):
        main_link = self.get_context_data().get('link_name') 
        return self.request.user.id == main_link.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))


class FacebookEditView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    this is for displaying the Facebook edit form in the template.
    '''

    template_name = 'social_media/Facebook/Facebook_edit.html'
    model = Facebook
    form_class = FacebookForm

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def form_valid(self, form):
        form.instance.author = Account.objects.get(user = self.request.user)
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('panel:modules_page', kwargs={'link_name': self.kwargs['link_name']})
    
    def test_func(self):
        main_link = self.get_object()
        return self.request.user.id == main_link.link_id.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))


class FacebookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    this is for deleting Facebook.
    '''

    template_name = 'dashboard/main_link.html'
    model = Facebook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # this is for send kwargs link_name with url
        link_name = self.kwargs['link_name']
        main_link = MainLink.objects.get(name=link_name)
        context['link_name'] = main_link

        return context


    def get_success_url(self):
        return reverse_lazy('panel:modules_page', kwargs={'link_name': self.kwargs['link_name']})
    
    def test_func(self):
        main_link = self.get_object()
        return self.request.user.id == main_link.link_id.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))