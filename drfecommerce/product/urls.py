
from rest_framework.routers import DefaultRouter

from product.views import BrandViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'product', ProductViewSet)
urlpatterns = router.urls
