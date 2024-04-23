from rest_framework import serializers
from backend.api.models import User, Event
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajout personnalisés au token
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_active'] = user.is_active
        token['avatar'] = user.avatar_url()

        return token


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password fields does not match")
        return data

    def create(self, validated_data):
        email = validated_data['email'].lower()  # Convertir l'email en minuscules
        
        user = User.objects.create_user(
            username = validated_data['username'],
            email = email,
            password = validated_data['password']
        )
        
        return user

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128)
    confirm_new_password = serializers.CharField(max_length=128)

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError("New password and confirm password do not match")
        return data
    
    def save(self, user):
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'is_single_event', 'recurrence_rules', 'date_start', 'date_end', 'time_start', 'time_end', 'is_supprime']

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'is_single_event', 'recurrence_rules', 'date_start', 'date_end', 'time_start', 'time_end']

    def create(self, validated_data):
        user = self.context['user']
        planning = user.planning
        validated_data['planning'] = planning
        return Event.objects.create(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar']  # inclure 'avatar' si vous souhaitez le retourner aussi

    def update(self, user, validated_data):
        avatar = validated_data.get('avatar', None)
        if avatar:
            user.avatar = avatar
            user.save()
        return user