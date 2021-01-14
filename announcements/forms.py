from django import forms
from . import models


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = models.Announcements
        fields = ['title', 'text']