from django import forms

class TextForm(forms.Form):
    comment = forms.CharField(label="", help_text="",widget=forms.Textarea(
        attrs={
            'id':"",
            'cols':30,
            'rows':10,
            'class':"rounded"
            }
        ))