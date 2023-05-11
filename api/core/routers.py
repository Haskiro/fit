from rest_framework.routers import DefaultRouter
from program.views import ProgramViewSet

router = DefaultRouter()

router.register("programs", ProgramViewSet)