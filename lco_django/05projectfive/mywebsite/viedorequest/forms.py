from django import forms

class VideoFrom(forms.Form):
    videoname = forms.CharField(max_length= 20,
    widget=forms.TextInput(attrs={
        'class': 'from-control',
        'placeholder' : 'Name',
        'id' : 'inputName'
    }))

    videodesc = forms.CharField(widget= forms.Textarea({
        'class': 'from-control',
        'row' : '5',
        'id' : 'comment',
        'placeholder' : 'Comment'
    }))