from django.db import router
from django.urls import path, include
from .views import home, latest, QuestionApi, rate_limiting

from rest_framework import routers

router = routers.DefaultRouter()
router.register("questions", QuestionApi)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    path('latest', latest, name='latest'),
    path('rate', rate_limiting, name='latest'),
]
