from django.db import models


class Paradign(models.Model):
    name = models.CharField(max_length=50)
     
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    paradign = models.ForeignKey(Paradign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)
    
    def __str__(self):
        return self.name
