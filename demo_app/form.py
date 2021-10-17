from . models import featured_items
from django import forms

class ModelForm(forms.ModelForm):
    class Meta:
        model=featured_items
        fields=['img','name','desc']
