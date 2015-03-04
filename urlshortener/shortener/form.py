from django import forms

class SubmitForm(forms.Form):
	urlLink = forms.URLField(label="", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'http://www.example.com'}))
