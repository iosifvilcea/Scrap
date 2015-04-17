from django import forms
from scrapyr_app.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email')
