
from django.urls import path
from rest_framework.routers import DefaultRouter
from tareas.views import TareaViewSet, CategoriaViewSet


router = DefaultRouter()
router.register(r'tareas',TareaViewSet, basename='tareas')
router.register(r'categorias',CategoriaViewSet, basename='categorias')

urlpatterns = router.urls

