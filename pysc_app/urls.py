from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet,TestViewSet,TestDetailViewSet

router = DefaultRouter()
router.register('question',QuestionViewSet, basename='question')
router.register('test',TestViewSet, basename='test')
router.register('test_detail',TestDetailViewSet, basename='test_detail')
urlpatterns = router.urls
