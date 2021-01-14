from django.urls import path 
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.AnnouncementList.as_view(), name='list'),
    path('create/', views.AnnouncementCreate.as_view(), name='create' )
]