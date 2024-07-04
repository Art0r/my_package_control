from django.urls import include, path
from rest_framework import routers
from core import views
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('resident', views.ResidentViewSet)
router.register('apartment', views.ApartmentViewSet)
router.register('package', views.PackageViewSet)
router.register('condo', views.CondoViewSet)
router.register('account', views.AccountViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]