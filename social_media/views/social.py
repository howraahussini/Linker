from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

from dashboard.views import CommonContextMixin



class SocialView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    '''
    this is for displaying all the social media .
    '''

    template_name = 'social_media/social.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
    def test_func(self):
        main_link = self.get_context_data().get('link_name') 
        return self.request.user.id == main_link.author_id

    def handle_no_permission(self):
        return redirect(reverse_lazy('web:home'))
