from django.db import models
from experiment.choices import LIKERT_SCALE

class Smartphone(models.Model):
    on_you_freq = models.IntegerField(choices=LIKERT_SCALE, default=1)
