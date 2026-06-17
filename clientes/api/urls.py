from rest_framework.routers import DefaultRouter
from clientes.api.views import ClienteViewSet

router = DefaultRouter()
router.register('clientes', ClienteViewSet, basename='cliente')
urlpatterns = router.urls