from django import forms


class SmsForm(forms.Form):
    to = forms.CharField(max_length=15)
    contents = forms.CharField(widget=forms.Textarea)