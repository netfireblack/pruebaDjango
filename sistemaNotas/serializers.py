from rest_framework import serializers
from .models import Alumno, Asignatura, Nota, Semestre


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('ialumnoid', 'vcnombre', 'vcapellido')


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('iasignaturaid', 'vcnombre')


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('inotaid', 'ialumnoid', 'isemestreid', 'iasignaturaid', 'dvalor')


class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = ('isemestreid', 'iano', 'inumero')