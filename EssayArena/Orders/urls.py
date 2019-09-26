from rest_framework_nested import routers
from .views import OrderViewset, BidViewSet

router = routers.SimpleRouter()

router.register(r'orders', OrderViewset)
bids_router = routers.NestedSimpleRouter(router, r'orders', lookup='order')
bids_router.register(r'bids', BidViewSet)

urlpatterns = router.urls + bids_router.urls
