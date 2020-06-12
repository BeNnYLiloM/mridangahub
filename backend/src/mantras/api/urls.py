from rest_framework.routers import DefaultRouter

from mantras.api.views import FamilyViewSet, GroupViewSet, MantraViewSet

router = DefaultRouter()
router.register('familiy', FamilyViewSet, basename='mantras')
router.register('group', GroupViewSet, basename='mantras')
router.register('mantra', MantraViewSet, basename='mantras')
urlpatterns = router.urls
