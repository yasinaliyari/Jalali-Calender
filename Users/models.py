from django.db import models
from django_jalali.db import models as jmodels


class CustomUser(models.Model):
    M = 1
    F = 2

    GENDER_CHOICES = (
        (M, "male"),
        (F, "female"),
    )
    username = models.CharField(max_length=256, name="username")
    full_name = models.CharField(max_length=256, name="full_name")
    gender = models.CharField(choices=GENDER_CHOICES, name="gender")
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField(name="birthday_date")
    ceremony_datetime = jmodels.jDateTimeField(name="ceremony_datetime")
    country = models.CharField(default="Iran", name="country")

    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split(" ")
        return {"first_name": first_name, "last_name": last_name}
