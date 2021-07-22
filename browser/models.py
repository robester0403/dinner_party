from django.db import models
from django.db.models.deletion import RestrictedError

# Create your models here.
# Make sure you register your map and make the migrations

class Recipe(models.Model):
    COUNTRY = [
        ('CDN', 'Canada'),
        ('CHN', 'China'),
        ('BZL', 'Brazil'),
        ('ITA', 'Italy'),
        ('USA', 'USA'),
    ]

    MAIN_TYPE = [
        ('NOOD', 'Noodle'),
        ('RICE', 'Rice'),
        ('DUMP', 'Dumpling'),
        ('BREA', 'Bread'),
        ('PIEE', 'Pie'),
    ]

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=3, choices=COUNTRY)
    sub_region = models.CharField(max_length=100)
    main_type = models.CharField(max_length=4, choices=MAIN_TYPE)
    recipe_text = models.TextField(blank = True)
    # unique identifier unique_identifier = name + username

    def __str__(self):
        return self.name