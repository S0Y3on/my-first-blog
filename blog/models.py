from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model): #모델(객체, object)을 정의하는 코드
#class 객체를 정의, Post 모델의 이름, models Post가 장고 모델임을 의미 (Post가 데이터베이스에 저장)
    #속성을 정의 (필드마다 어떤 종류의 데이터 타입을 가지는지 정함)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #models.CharField 글자 수가 제한된 텍스트 정의 (ex 글제목)
    #models.TextField 글자 수에 제한이 없는 텍스트 정의 (ex 글내용)
    #models.DateTimeField 날짜와 시간
    #models.ForeignKey 다른 모델에 대한 링크 (외래키)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
