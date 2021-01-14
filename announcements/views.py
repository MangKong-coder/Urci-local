from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.

class AnnouncementList(generic.ListView):
    model = models.Announcements 

class AnnouncementDetail(generic.DetailView):
    model = models.Announcements

class AnnouncementCreate(generic.CreateView, LoginRequiredMixin):
    # form_class = forms.AnnouncementForm
    fields = ('title', 'text')
    model = models.Announcements

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AnnouncementDelete(generic.DeleteView, LoginRequiredMixin):
    model = models.Announcements
    success_url = reverse_lazy("announcements:list")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)




