from django import forms

class UserInput(forms.Form):
    # Not sure which field type to use
    bar_type = forms.ChoiceField()
    drink_type = forms.ChoiceField()
    price = forms.ChoiceField()
    distance = forms.ChoiceField()
