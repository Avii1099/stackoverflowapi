from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("apiv", views.ApiList, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)),
    path('click/', views.clickbutton),
    path('getdata/<str:value>', views.getdata)
]
