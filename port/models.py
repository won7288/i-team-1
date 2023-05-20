from django.db import models

<<<<<<< HEAD
=======

>>>>>>> 741aabf5e6bea439155dbeee594491b0aba3d901
class myprofile(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

class Portlist(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
<<<<<<< HEAD
=======

>>>>>>> 741aabf5e6bea439155dbeee594491b0aba3d901
