from django.db import models


class WorkoutDetails(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    reps = models.IntegerField(verbose_name="Reps")
    sets = models.IntegerField(verbose_name="Sets")
    kg = models.IntegerField(verbose_name="Kg")
    date = models.DateField(verbose_name="Date")

    def __str__(self):
        return str(self.id)
