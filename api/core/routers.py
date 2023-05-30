from rest_framework.routers import DefaultRouter
from program.views import ProgramViewSet
from exercise.views import ExerciseViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register("programs", ProgramViewSet)
router.register("exercises", ExerciseViewSet)
router.register('auth', UserViewSet)
