from django.db import models


class Laureate(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    contribution = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.year})"
