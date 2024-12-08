from django.contrib import admin
from django.urls import path ,include
from website import views


urlpatterns = [
    path('', views.index_view ),
    path('about/',views.about_view),
    path('content/',views.content_view)
    

]
