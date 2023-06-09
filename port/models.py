from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class my_detail(models.Model):      #본인 이력 상세페이지
    project_title = models.CharField(max_length=20)
    project_image = models.ImageField()
    content = models.TextField()
    create_date = models.DateTimeField()



class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    content = models.TextField()

class Profile(models.Model):
    image = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=50)
    career = models.CharField(max_length=500)