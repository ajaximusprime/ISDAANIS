from django.db import models


class Species(models.Model):
    species_id = models.CharField(max_length=30, primary_key=True)
    species_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Origin(models.Model):
    origin = models.CharField(max_length=30, primary_key=True)
    date = models.DateTimeField()


class Vessel(models.Model):
    vessel_id = models.CharField(max_length=30)
    vessel_name = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user_type = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)


class DailyTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    date = models.DateTimeField()
