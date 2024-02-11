from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import FormView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


from .models import Account
from .forms import SignUpForm, LoginForm, AccountForm
from dashboard.views import CommonContextMixin


class SignUpView(FormView):
    """
    class SignUpView is for displaying signup form in template.
    """

    template_name = "registration/signup.html"
    form_class = SignUpForm
    redirect_authentication_user = True
    success_url = reverse_lazy("dashboard:dashboard")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("dashboard:dashboard")
        return super(SignUpView, self).get(*args, **kwargs)
    

class LoginView(LoginView):
    '''
    this is for displaying the login form in the template.
    '''

    template_name = 'registration/login.html'
    form_class = LoginForm
    redirect_authentication_user = True
    success_url = reverse_lazy('dashboard:dashboard')


class AccountView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    this is for displaying the accounts user information in the template.
    '''

    template_name = 'registration/account.html'
    model = Account
    form_class = AccountForm


    def form_valid(self, form):
        self.request.user = form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('panel:modules_page', kwargs={'link_name': self.kwargs['link_name']})
    
    def test_func(self):
        main_link = self.get_object()
        return self.request.user.id == main_link.user_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))