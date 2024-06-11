from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'peterparker@sony.com'})
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peter'})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parker'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'theamazingspiderman'
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'i love gwen'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'i love gwen'
        self.fields['password2'].label = 'Re-Enter Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class AddRecord(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Otto Octavious', 'class': 'form-control'}),
        label='Name'
    )
    alias = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Dr. Octopus', 'class': 'form-control'}),
        label='Alias'
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Got 4 mechanical robotical arms with claws.', 'class': 'form-control'}),
        label='Description'
    )
    powers = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Physical Strength and Better Movement Speed', 'class': 'form-control'}),
        label='Powers'
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'NYC', 'class': 'form-control'}),
        label='City'
    )
    status = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Professor at Oscorp', 'class': 'form-control'}),
        label='Status'
    )

    class Meta:
        model = Record
        exclude = ('user',)
