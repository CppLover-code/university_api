from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet, SubjectViewSet, StudentViewSet

router = DefaultRouter()

router.register(r"teachers", TeacherViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"students", StudentViewSet)

urlpatterns = router.urls
