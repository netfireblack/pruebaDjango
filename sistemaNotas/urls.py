from rest_framework import routers
from .api import AlumnoViewSet, AsignaturaViewSet, NotaViewSet, SemestreViewSet


router = routers.DefaultRouter()

router.register('universidad/alumnos', AlumnoViewSet, 'alumnos')
router.register('universidad/asignaturas', AsignaturaViewSet, 'asignaturas')
router.register('universidad/notas', NotaViewSet, 'notas')
router.register('universidad/semetres', SemestreViewSet, 'semestres')

urlpatterns = router.urls