from typing import Any
from django.shortcuts import redirect 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView


from dashboard.views import CommonContextMixin
from accounts.models import Account
from dashboard.models import MainLink
from panel.models import Profile

from panel.forms import ProfileForm


class ProfileEditView(CommonContextMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    this is for displaying the profile edit form in the template.
    '''

    template_name = 'panel/profile/profile_edit.html'
    model = Profile
    form_class = ProfileForm

    
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