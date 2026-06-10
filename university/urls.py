from rest_framework.routers import DefaultRouter

from .views import (
    TeacherViewSet,
    SubjectViewSet,
    StudentViewSet,
    StudentRegistrationViewSet,
)

router = DefaultRouter()

router.register(r"teachers", TeacherViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"students", StudentViewSet)

router.register(
    r"register-student",
    StudentRegistrationViewSet,
    basename="register-student"
)

urlpatterns = router.urls