from django.db import models

class my_detail(models.Model):      #본인 이력 상세페이지
    project_title = models.CharField(max_length=20)
    project_image = models.ImageField()
    content = models.TextField()
    create_date = models.DateTimeField()

class user_detail(models.Model):    #다른유저 이력 상세페이지
    project_title = models.CharField(max_length=20)
    project_image = models.ImageField()
    content = models.TextField()
    create_date = models.DateTimeField()
    write_question = models.CharField(max_length=50)