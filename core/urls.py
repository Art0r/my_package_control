from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register('resident', views.ResidentViewSet)
router.register('apartment', views.ApartmentViewSet)
router.register('package', views.PackageViewSet)
router.register('condo', views.CondoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token_handling/', views.TokenHandling.as_view(), name='create_token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]