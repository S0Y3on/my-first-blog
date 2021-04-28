from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    path('user_list/', views.user_list, name='user_list'),
    # path('accounts/', include('allauth.urls')),
    # url(r'^accounts/', include('allauth.urls')),  # <- 추가
]
