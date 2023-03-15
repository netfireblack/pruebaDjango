from .models import Alumno, Asignatura, Nota, Semestre
from rest_framework import viewsets, permissions, filters
from .serializers import AlumnoSerializer, AsignaturaSerializer, NotaSerializer, SemestreSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['vcapellido']
    

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['vcnombre']


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NotaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['dvalor']

class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SemestreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['iano', 'inumero']