from . import views
from django.urls import path

urlpatterns = [
     path('', views.home, name='home'),
     path('signup/',views.signup , name='signup'),
     path('update/<int:id>',views.update,name='update'),
     path('delete/<int:id>',views.delete,name='delete'),
]
