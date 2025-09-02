from django import forms
from django.core.exceptions import ValidationError
from Users.models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "full_name",
            "gender",
            "national_code",
            "birthday_date",
            "ceremony_datetime",
            "country",
        ]

    def clean_national_code(self):
        code = self.cleaned_data.get("national_code")
        if len(code) != 10 or not code.isdigit():
            raise ValidationError(
                "The national code must be 10 digits and only contain numbers."
            )
        return code

    def clean_full_name(self):
        name = self.cleaned_data.get("full_name")
        parts = name.split(" ")

        if len(parts) != 2:
            raise ValidationError(
                "Enter your first and last name with a space between them."
            )
        first, last = parts
        if not first.istitle() or not last.istitle():
            raise ValidationError(
                "First and last names must start with a capital letter."
            )
        return name
