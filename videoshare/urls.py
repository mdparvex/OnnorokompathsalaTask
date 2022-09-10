from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('likepost', views.likepost, name='likepost'),
    path('dislikepost', views.dislikepost, name='dislikepost'),
    path('view', views.viewcount, name='viewcount'),
    path('detail/<str:id>', views.detail, name='detail'),
    
]