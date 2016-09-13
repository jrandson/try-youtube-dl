from django import forms

class UploadFileForm(forms.Form):
    file_name = forms.FileField()

    

