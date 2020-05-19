from django import forms

class addRoastBoast(forms.Form):
    RoastOrBoast = (
        (True, 'Roast'),
        (False, 'Boast')
        )
    roastBoast = forms.ChoiceField(choices=RoastOrBoast)
    post = forms.CharField(max_length=280)