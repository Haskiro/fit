from rest_framework.exceptions import ValidationError, ParseError, NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.serializers import UserSerializer
from authentication.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from program.models import Program
from django.core.mail import send_mail



# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=request.data['email'])

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token)}
        send_mail(
            subject = "FIT registration",
            message = "Thanks for your registration! Good luck!",
            from_email = "fit@club.com",
            recipient_list = [request.data['email']],
            fail_silently = False
        )
        return response

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email must not be empty'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'password must not be empty'})

        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token), 'refresh': str(refresh)}
        return response
        
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def getUser(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def add_program_to_user(self, request):
        data = request.data
        user = request.user
        currentData = self.serializer_class(user).data
        for program_id in data:
            try:
                if (program_id not in currentData['programs']):
                    program = Program.objects.get(id=program_id)
                    currentData['programs'].append(program)
                else:
                    return Response({"error": "program with id=" + str(program_id) + " already added"}, 402)

            except Program.DoesNotExist:
                return Response(
                    {"error": "program with id=" + program_id + "does not exist"}
                )
        user.programs.set(currentData['programs'])
        user.save()
        

        return Response({"message": "programs added"}, 201)
