from rest_framework import routers
from .views import RegistrationView, LoginAPIView

router = routers.SimpleRouter()

router.register(r'signup', RegistrationView)
router.register(r'login', LoginAPIView)

urlpatterns = router.urls

