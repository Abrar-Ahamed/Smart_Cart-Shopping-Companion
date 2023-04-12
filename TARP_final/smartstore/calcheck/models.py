from django.db import models

# Create your models here.
class Diary(models.Model):
    name = models.CharField(max_length=100)
    energy = models.IntegerField(null=True)
    protein = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    sugar = models.FloatField(null=True)
    calcium = models.IntegerField(null=True)
    potassium = models.IntegerField(null=True)
    sodium = models.IntegerField(null=True)
    fa_sat = models.FloatField(null=True)
    fa_mono = models.FloatField(null=True)
    fa_poly = models.FloatField(null=True)
    cholest = models.IntegerField(null=True)


    def __str__(self):
        return self.name