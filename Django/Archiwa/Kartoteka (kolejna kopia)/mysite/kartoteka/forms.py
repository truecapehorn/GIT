from django.contrib.auth.models import User
from .models import Row
from django.forms import ModelForm


# class EntryForm(ModelForm):
#     class Meta:
#         model = Row
#
#     def clean_author(self):
#         if not self.cleaned_data['author']:
#             return User()
#         return self.cleaned_data['author']
#
#     def clean_last_modified_by(self):
#         if not self.cleaned_data['last_modified_by']:
#             return User()
#         return self.cleaned_data['last_modified_by']