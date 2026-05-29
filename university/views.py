from rest_framework import viewsets

from .models import Teacher, Student, Subject
from .serializer import TeacherSerializer, StudentSerializer, SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.object.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.object.all()
    serializer_class = StudentSerializer

class subjectViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Subject.object.all()
    serializer_class = SubjectSerializer

