# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    ialumnoid = models.AutoField(db_column='iAlumnoID', primary_key=True)  # Field name made lowercase.
    vcnombre = models.CharField(db_column='vcNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vcapellido = models.CharField(db_column='vcApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alumno'


class Asignatura(models.Model):
    iasignaturaid = models.AutoField(db_column='iAsignaturaID', primary_key=True)  # Field name made lowercase.
    vcnombre = models.CharField(db_column='vcNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Asignatura'


class Nota(models.Model):
    inotaid = models.AutoField(db_column='iNotaID', primary_key=True)  # Field name made lowercase.
    ialumnoid = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='iAlumnoID', blank=True, null=True)  # Field name made lowercase.
    isemestreid = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='iSemestreID', blank=True, null=True)  # Field name made lowercase.
    iasignaturaid = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='iAsignaturaID', blank=True, null=True)  # Field name made lowercase.
    dvalor = models.DecimalField(db_column='dValor', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nota'


class Semestre(models.Model):
    isemestreid = models.AutoField(db_column='iSemestreID', primary_key=True)  # Field name made lowercase.
    iano = models.IntegerField(db_column='iAno', blank=True, null=True)  # Field name made lowercase.
    inumero = models.IntegerField(db_column='iNumero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Semestre'
