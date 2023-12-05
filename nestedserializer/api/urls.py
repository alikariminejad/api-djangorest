from django.urls import path, include
from api.views import ProfileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', ProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
]