from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
#post_list view를 루트 url로 할당 
