from product.viewset import ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products-abc', ProductViewset, basename='products')
for path in router.urls:
    print(path)
urlpatterns = router.urls