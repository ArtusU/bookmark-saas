from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    BASIC = "basic"
    PRO = "pro"

    CHOICES_PLANS = ((BASIC, "Basic"), (PRO, "Pro"))

    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )
    plan = models.CharField(max_length=20, choices=CHOICES_PLANS, default=BASIC)
    subscription = models.CharField(max_length=100, default="")
