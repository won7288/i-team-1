from django.db import models

class my_detail(models.Model):      #본인 이력 상세페이지
    main_title = models.CharField(max_length=20)
    project_title = models.CharField(max_length=20)
    project_image = models.ImageField()
    content = models.TextField()
    create_date = models.DateTimeField()

class User_detail(models.Model):    #다른유저 이력 상세페이지
    main_title = models.CharField(max_length=20)
    project_title = models.CharField(max_length=20)
    project_image = models.ImageField()
    content = models.TextField()
    create_date = models.DateTimeField()
    write_question = models.CharField(max_length=50)