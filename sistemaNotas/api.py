from .models import Alumno, Asignatura, Nota, Semestre
from rest_framework import viewsets, permissions
from .serializers import AlumnoSerializer, AsignaturaSerializer, NotaSerializer, SemestreSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializer
    

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NotaSerializer
    

class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SemestreSerializer