from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TransacaoViewSet


router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('transacoes', TransacaoViewSet)


urlpatterns = router.urls