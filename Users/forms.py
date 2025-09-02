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
