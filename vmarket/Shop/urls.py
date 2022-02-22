from multiprocessing.spawn import import_main_path
from .views import shopViewset
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Shop', shopViewset, basename= 'Shop')

urlpatterns = [
    path('',include(router.urls))
]