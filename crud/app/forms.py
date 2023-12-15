from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.BooleanField(required=False)
    # birthday = forms.DateField()
