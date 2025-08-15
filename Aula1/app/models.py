from django.db import models

CATEGORIES = [
    ('HORROR','Terror'),
    ('COMEDY', 'Comédia'),
    ('FICCTION', 'Ficção'),
    ('DOCUMENTARY', 'Documentário'),
    ('ACTION', 'Ação'),
]

class Movie(models.Model):
   title = models.CharField(max_length=300, null=False)
   description = models.CharField(max_length=1000)
   category = models.CharField(max_length=100, choices=CATEGORIES)
   published_date =  models.DateField()
   photo = models.TextField()
   classification = models.IntegerField