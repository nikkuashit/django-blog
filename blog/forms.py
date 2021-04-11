from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }
    ))
    descreption = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Descreption'
        }
    ))
