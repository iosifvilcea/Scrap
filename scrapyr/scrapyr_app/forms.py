from django import forms
from scrapyr_app.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email')

class StockFeedForm(forms.Form):
    sf_input = forms.CharField(label="Company Name")

