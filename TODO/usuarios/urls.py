
from django.urls import path
from usuarios.views import RolViewSet, UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios',UsuarioViewSet, basename='usuarios')
router.register(r'rol',RolViewSet, basename='rol')

urlpatterns = router.urls

