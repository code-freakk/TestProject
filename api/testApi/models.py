from django.db import models


class Form(models.Model):
    """
    """
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    marry = models.CharField(max_length=100)
    resume = models.FileField(default=None, null=True)