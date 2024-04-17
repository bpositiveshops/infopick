from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username:
            self.cleaned_data['email'] = username
        return cleaned_data
