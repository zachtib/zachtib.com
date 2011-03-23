from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password (confirm)', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    email_confirm = forms.EmailField(label='Email (confirm)')
    firstname = forms.CharField(label='First Name (optional)', required=False)
    lastname = forms.CharField(label='Last Name (optional)', required=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password', '')
        password_confirm = self.cleaned_data.get('password_confirm', '')
        print password, password_confirm
        if password != password_confirm or password == '':
            raise forms.ValidationError('Passwords do not match.')
        return password

    def clean_email_confirm(self):
        email = self.cleaned_data.get('email', '')
        email_confirm = self.cleaned_data.get('email_confirm', '')
        print email, email_confirm
        if email != email_confirm or email == '':
            raise forms.ValidationError('Emails do not match.')
        return email
