from django.contrib.auth.forms import UserCreationForm

from catalog.models import StyleFormMixin
from .models import CustomUser
from django import forms


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text="Необязательное поле. Введите номер телефона")
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ("email", "username", "phone_number", "country", "avatar", "password1", "password2")


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("номер телефона должен состоять только из цифр")
        return phone_number