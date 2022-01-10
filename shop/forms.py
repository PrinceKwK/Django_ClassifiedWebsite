from django import forms 

class NewAdForm(forms.Form):
    title = forms.CharField(max_length=70)
    description = forms.Textarea()
    price = forms.CharField(max_length=20)
