from django import forms

class FormCreateDog(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': "form-control"}))
    breed = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': "form-control"}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control"}))
    owner_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': "form-control"}))


class SearchBreed(forms.Form):
    breed = forms.CharField(max_length=40, required=False)