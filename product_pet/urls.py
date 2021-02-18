from django.db import router
from django.urls import include,path
from rest_framework import routers
from .views import CategoryViewSet, ProductPetViewset


router=routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'productpets',ProductPetViewset, basename='productpets')
urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='api_productpet'))
]