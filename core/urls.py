from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MedicoRegisterView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoRegisterView, PacienteViewSet


router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)


urlpatterns = [
     path('', include(router.urls)),
    path('registro/', MedicoRegisterView.as_view(), name='registro'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]