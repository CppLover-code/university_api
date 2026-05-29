from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet, subjectViewSet, StudentViewSet

router = DefaultRouter()

router.register(r"teachers", TeacherViewSet)
router.register(r"subjects", subjectViewSet)
router.register(r"students", StudentViewSet)

urlpatterns = router.urls
