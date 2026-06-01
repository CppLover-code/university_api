from rest_framework import viewsets

from .models import Teacher, Student, Subject
from .serializer import TeacherSerializer, StudentSerializer, SubjectSerializer

from .permissions import IsTeacherOrReadOnly

from rest_framework.permissions import IsAuthenticated

from users.permissions import (
    IsAdmin,
    IsTeacherOrAdmin
)

# viewsets.ModelViewSet - Это готовый CRUD.
# queryset - Какие данные брать из базы.
# serializer_class - Как превращать данные в JSON.
class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    permission_classes = [IsAdmin]

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [IsAdmin]

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    permission_classes = [IsTeacherOrAdmin]

