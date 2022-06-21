from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class Form(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    gender = forms.ChoiceField(label='Gender', choices=(('Male', 'Male'), ('Female', 'Female')), widget=forms.RadioSelect)
    age = forms.IntegerField(label='Age')
    choices = ((1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'C2'))
    english_level = forms.ChoiceField(choices=choices)

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        gender = cleaned_data.get('gender')
        english_level = cleaned_data.get('english_level')
        if gender == 'Male' and (age < 20 or int(english_level) < 4):
            raise ValidationError('Validation Error')
        elif gender == 'Female' and (age < 22 or int(english_level) < 2):
            raise ValidationError('Validation Error')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('WRONG password or username!')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    rep_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        rep_password = cleaned_data.get('rep_password')

        if password != rep_password:
            raise forms.ValidationError('Passwords don\'t match!')


class PassChangeForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    rep_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    rep_new_password = forms.CharField(label='Repeat new password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        rep_password = cleaned_data.get('rep_password')
        new_password = cleaned_data.get('new_password')
        rep_new_password = cleaned_data.get('rep_new_password')

        if new_password != rep_new_password:
            raise forms.ValidationError('New passwords don\'t match!')

        if password != rep_password:
            raise forms.ValidationError('New passwords don\'t match!')


class GetComments(forms.Form):
    some_words = forms.CharField(label='Words in comments:', max_length=100)
    only_user_com = forms.BooleanField(required=False)

