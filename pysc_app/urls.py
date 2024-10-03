from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet,TestViewSet

router = DefaultRouter()
router.register('question',QuestionViewSet, basename='question')
router.register('test',TestViewSet, basename='test')
urlpatterns = router.urls
