from django import forms


class InputForm(forms.Form):
    post = forms.CharField(label='', widget=forms.Textarea(attrs={'id':'post-text'}))

class FileForm(forms.Form):
    upload_file = forms
    
