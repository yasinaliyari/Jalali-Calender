import jdatetime
from django.db import models
from django_jalali.db import models as jmodels


class CustomUser(models.Model):

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female"),
    )
    username = models.CharField(max_length=256, name="username")
    full_name = models.CharField(max_length=256, name="full_name")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, name="gender")
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField(name="birthday_date")
    ceremony_datetime = jmodels.jDateTimeField(name="ceremony_datetime")
    country = models.CharField(max_length=10, default="Iran", name="country")

    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split(" ")
        return {"first_name": first_name, "last_name": last_name}

    def get_age(self):
        today = jdatetime.date.today()
        years = today.year - self.birthday_date.year

        if (today.month, today.day) < (
            self.birthday_date.month,
            self.birthday_date.day,
        ):
            years -= 1

        return years

    def is_birthday(self):
        today = jdatetime.date.today()
        if (self.birthday_date.month, self.birthday_date.day) == (
            today.month,
            today.day,
        ):
            return True
        return False
