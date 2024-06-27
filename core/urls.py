from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register('resident', views.ResidentViewSet)
router.register('apartment', views.ApartmentViewSet)
router.register('package', views.PackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]