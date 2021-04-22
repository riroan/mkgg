from django import forms
from search.models import User

class SearchForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userName']
        widgets = {'userName':forms.TextInput(attrs={'name':'userName'})}