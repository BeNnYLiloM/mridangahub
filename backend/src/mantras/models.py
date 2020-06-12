from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=255)

class Group(models.Model):
    name = models.CharField(max_length=255)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)

class Mantra(models.Model):
    name = models.CharField(max_length=255)
    scheme = models.TextField()
    visual_scheme = models.TextField()
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
