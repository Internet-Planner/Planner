from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, PasswordResetSerializer
from .models import Planning
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from backend.api.utils.token import account_activation_token
from django.contrib.auth.tokens import default_token_generator
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from backend.api.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Vérifie si l'utilisateur existe
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": 4098}, status=status.HTTP_400_BAD_REQUEST)

        # Vérifie si le mot de passe est correct
        if not user.check_password(password):
            return Response({"message": 4098}, status=status.HTTP_400_BAD_REQUEST)

        # Vérifie si l'utilisateur est actif
        if not user.is_active:
            return Response({"message": 4406}, status=status.HTTP_403_FORBIDDEN)

        # Si tout est OK on génère le token
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_data = serializer.validated_data
        return Response(token_data, status=status.HTTP_200_OK)
        


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/token",
        "/api/token/refresh",
    ]
    return Response(routes)


@api_view(["POST"])
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return Response(
            {"message": "Account activated successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
    else:
        return Response(
            {"message": "Activation link is invalid"},
            status=status.HTTP_400_BAD_REQUEST,
        )


def activateEmail(request, user, to_email):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    subject = "Activate your Planner account"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

    html_content = render_to_string(
        "account_activation_email.html",
        {
            "user": user,
            "activation_link": f"http://{settings.DOMAIN}/activate/{uid}/{token}",
            "protocol": "https" if request.is_secure() else "http",
        },
    )

    # Extraire le texte brut de l'e-mail
    text_content = strip_tags(html_content)

    # Envoyer l'e-mail
    send_result = send_mail(
        subject, text_content, from_email, [to_email], html_message=html_content
    )

    if send_result:
        return Response(
            {"message": "Email sent successfully"}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Failed to send email"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def forgotPassword(request):
    email = request.data.get('email')
    User = get_user_model()

    try:
        user = User.objects.get(email=email)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        subject = "Password Reset Request"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email

        html_content = render_to_string(
            "password_reset_email.html",
            {
                "user": user,
                "reset_password_link": f"http://{settings.DOMAIN}/reset-password/{uid}/{token}",
                "protocol": "https" if request.is_secure() else "http",
            },
        )

        text_content = strip_tags(html_content)
        
        # Envoie l'e-mail
        send_mail(subject, text_content, from_email, [to_email], html_message=html_content, fail_silently=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except User.DoesNotExist:
        # Si l'utilisateur n'existe pas, retourne quand même un statut 200
        return Response(status=status.HTTP_204_NO_CONTENT)
   

@api_view(["POST"])
def resetPassword(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None:
        # Vérifier si le token est valide
        if default_token_generator.check_token(user, token):

            serializer = PasswordResetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # Créer automatiquement un planning pour l'utilisateur nouvellement créé
        Planning.objects.create(user=user)

        # Envoyer l'e-mail d'activation
        activateEmail(request, user, user.email)

        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )
    return Response({"message": "Failed to register"}, status=status.HTTP_400_BAD_REQUEST)
