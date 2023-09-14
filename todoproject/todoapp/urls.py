from .import views
from django.urls import path, include
urlpatterns = [
path('',views.newapp,name='newapp'),
path('delete/<int:taskid>',views.delete,name='delete'),
path('update/<int:id>',views.update,name='update'),
path('cbvhome/',views.taskview.as_view(),name='cbvhome'),
path('cbvdetails/<int:pk>/',views.details.as_view(),name='cbvdetails'),
path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete')
]