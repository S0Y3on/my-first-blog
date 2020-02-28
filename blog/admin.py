from django.contrib import admin
from .models import Post
#앞 장에서 정의한 Post모델을 가져온다.

# Register your models here.

admin.site.register(Post)
#관리자 페이지에서 만든 모델을 보기위해 모델 등록 
