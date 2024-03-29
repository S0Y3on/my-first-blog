from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post_search', views.post_search, name='post_search'),
    path('post_test', views.post_test, name='post_test'),
    path('xxe_index', views.index, name='xxe_index'),
    path('xxe_result', views.result, name='xxe_result'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # path(r'', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    # url('accounts/', include('allauth.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#post_list view를 루트 url로 할당
