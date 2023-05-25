from django.db import models


class UserProfile(models.Model): #유저 프로필 데이터 모델
    subject = models.CharField(max_length=200)
    content = models.TextField()

class Portlist(models.Model): #이력 및 경력 모델
    subject = models.CharField(max_length=200)
    content = models.TextField()

class MyPort_details(models.Model): #이력 및 경력 목록을 클릭해서 이동할 시 자세하게 나오는 모델
    subject = models.CharField(max_length=200)
    content = models.ImageField()
    content = models.TextField()

class Users_detail(models.Model): # 다른 유저의 이력 및 경력 클릭시 상세 페이지 모델
    subject = models.CharField(max_length=200)
    content = models.ImageField()
    content = models.TextField()

class Question(models.Model): # 질문 모델
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model): # 답변 모델
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()