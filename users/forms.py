from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, UserProfile


class RegForm(forms.ModelForm):
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Логин',
            'email': 'Электронная почта',
            'password': 'Пароль',
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'username': {
                'required': "Это поле обязательно для заполнения.",
            },
            'password': {
                'required': "Это поле обязательно для заполнения.",
                'invalid': "Убедитесь, что это значение содержит только буквы, цифры и @/./+/-/_ символы.",
                'max_length': "Убедитесь, что это значение содержит не более 150 символов."
            },
            'email': {
                'required': "Это поле обязательно для заполнения.",
                'invalid': "Введите корректный адрес электронной почты."
            }
        }
        help_texts = {
            'username': '',
        }

    def check_password(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 == password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")


class RussianLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'


class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about_me', 'gender', 'interests', 'link_other_social_networks']
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 5}),
            'gender': forms.Select(choices=UserProfile.gender_choices),
            'interests': forms.SelectMultiple(choices=UserProfile.interest_choices),
            'link_other_social_networks': forms.Textarea(attrs={'rows': 3})
        }
        labels = {
            'about_me': 'О себе',
            'gender': 'Пол',
            'interests': 'Интересы в творчестве',
            'link_other_social_networks': 'Ссылки на другие соцсети'
        }
