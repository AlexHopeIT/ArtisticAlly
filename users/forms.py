from django import forms
from .models import CustomUser


class RegForm(forms.ModelForm):
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def check_password(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 == password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")
