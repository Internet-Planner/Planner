import jwt, datetime
from django.contrib.auth import login, authenticate
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Event, Video, Planning, RevokedToken
from .serializer import UserSerializer, EventSerializer, VideoSerializer, PlanningSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all().order_by('id')
    serializer_class = PlanningSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

# ***************************************************************************************************

class RegisterView(APIView):
    def post(self, request):
       serializer = UserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       
       return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password'] 
        user = User.objects.filter(email=email).first() 

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # Création du jwt (JSON Web Token) payload = info du token
        payload = { 
            'id': user.id, # ID de l'utilisateur
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), # temps d'expiration du token (60 minutes)
            'iat': datetime.datetime.utcnow() # date de création du token
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256') # encodage du token avec l'algorithme HS256
        
        user = User.objects.filter(id=payload['id']).first() # récupération de l'utilisateur à partir de l'ID du token

        userData = {
            'id': user.id,
            'nick_name': user.nick_name,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        response = Response() 
        response.set_cookie(key='jwt', value=token, httponly=True) # envoi du token dans un cookie, httponly=True pour empêcher l'accès au cookie depuis le JavaScript
        response.data = userData # envoi du user dans la réponse JSON

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt') # récupération du token dans le cookie

        if not token:
            # raise AuthenticationFailed('Unauthenticated!')
            raise AuthenticationFailed('No token!')
        
        # décodage du token avec l'algorithme HS256
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256']) 
        except jwt.ExpiredSignatureError:
            # raise AuthenticationFailed('Unauthenticated!')
            raise AuthenticationFailed('Expired token!')
        
        user_id = payload.get('id') 
        if not user_id: 
            raise AuthenticationFailed('Invalid token!')
        
        user = User.objects.filter(id=payload['id']).first() # récupération de l'utilisateur à partir de l'ID du token
        serializer = UserSerializer(user) 
    
        return Response(serializer.data) # renvoi des données de l'utilisateur dans la réponse JSON

class LogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt') # récupération du token dans le cookie
        if token:
            RevokedToken.objects.create(token=token)  # Ajoutez le token à la liste des tokens révoqués en BDD
        response = Response()
        response.delete_cookie('jwt') # Supprimez le cookie 'jwt' des cookies 
        response.data = {
            'message': 'logout success'
        }

        return response
    
    
