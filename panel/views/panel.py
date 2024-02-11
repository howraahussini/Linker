from typing import Any
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from dashboard.views import CommonContextMixin
from dashboard.models import MainLink


class ModulesPageView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    '''
    This is the page that displays the main link modules section and
    I decided that this is the main page of the panel.
    '''

    template_name = 'panel/modules_page.html'
    model = MainLink


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def test_func(self):
        main_link = self.get_context_data().get('link_name') 
        return self.request.user.id == main_link.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))

