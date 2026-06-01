from rest_framework import viewsets

from .models import Teacher, Student, Subject
from .serializer import TeacherSerializer, StudentSerializer, SubjectSerializer

from .permissions import IsTeacherOrReadOnly

from rest_framework.permissions import IsAuthenticated

# viewsets.ModelViewSet - Это готовый CRUD.
# queryset - Какие данные брать из базы.
# serializer_class - Как превращать данные в JSON.
class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # permission_classes = [IsTeacherOrReadOnly]

