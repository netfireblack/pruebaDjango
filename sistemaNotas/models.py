from django.db import models


class Alumno(models.Model):
    ialumnoid = models.AutoField(db_column='iAlumnoID', primary_key=True)
    vcnombre = models.CharField(db_column='vcNombre', max_length=100, blank=True, null=True)
    vcapellido = models.CharField(db_column='vcApellido', max_length=100, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'Alumno'


class Asignatura(models.Model):
    iasignaturaid = models.AutoField(db_column='iAsignaturaID', primary_key=True)
    vcnombre = models.CharField(db_column='vcNombre', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Asignatura'


class Nota(models.Model):
    inotaid = models.AutoField(db_column='iNotaID', primary_key=True)
    ialumnoid = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='iAlumnoID', blank=True, null=True) 
    isemestreid = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='iSemestreID', blank=True, null=True)
    iasignaturaid = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='iAsignaturaID', blank=True, null=True)
    dvalor = models.DecimalField(db_column='dValor', max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nota'


class Semestre(models.Model):
    isemestreid = models.AutoField(db_column='iSemestreID', primary_key=True)
    iano = models.IntegerField(db_column='iAno', blank=True, null=True)
    inumero = models.IntegerField(db_column='iNumero', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Semestre'
