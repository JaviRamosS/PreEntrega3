from django import forms

class FormCreateDog(forms.Form):
    name = forms.CharField(max_length=40)
    breed = forms.CharField(max_length=40)
    age = forms.IntegerField()
    owner_name = forms.CharField(max_length=40)


class SearchBreed(forms.Form):
    breed = forms.CharField(max_length=40, required=False)