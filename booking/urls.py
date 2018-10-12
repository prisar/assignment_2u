from rest_framework.routers import DefaultRouter

from .api import ScreenViewSet, SeatViewSet

router = DefaultRouter()
router.register(r'screens', ScreenViewSet)
router.register(r'seats', SeatViewSet)

urlpatterns = router.urls