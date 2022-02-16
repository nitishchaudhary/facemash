from django.urls import path
from .import views

urlpatterns =[
    path('', views.index ,name = 'index'),
    path('ChangeImage1' , views.change_image1 , name = 'change_image'),
    path('ChangeImage2' , views.change_image2 , name = 'change_image'),
    path('ranking' , views.ranking , name= 'about')
]