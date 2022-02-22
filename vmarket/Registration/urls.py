
from .views import AppUserViewset
from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path,include


router  = DefaultRouter()
router.register('Registration', AppUserViewset, basename= 'Registration')

urlpatterns = [
    path('',include(router.urls))
]