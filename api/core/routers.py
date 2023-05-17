from rest_framework.routers import DefaultRouter
from program.views import ProgramViewSet
from exercise.views import ExerciseViewSet

router = DefaultRouter()

router.register("programs", ProgramViewSet)
router.register("exercises", ExerciseViewSet)