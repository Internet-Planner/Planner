from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'role')

# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Event
#         fields=('id', 'isLive','title', 'duration', 'reccurence', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Video
#         fields=('id', 'link','description','thumbnail', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')

# class PlanningSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Planning
#         fields=('id', 'name','description', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'role', 'nick_name', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')
#         extra_kwargs = {'password': {'write_only': True}} # Le champ 'password' ne sera pas renvoyé dans les réponses JSON (write_only=True)
        
#     # Créer un nouvel utilisateur à partir des données validées
#     def create(self, validated_data):
#         password = validated_data.pop('password', None) # Extrait 'password' des données validées
#         email = validated_data.pop('email', None) # Extrait 'email' des données validées
#         instance = self.Meta.model(**validated_data) # Création d'une nouvelle instance du modèle User avec les données validées
        
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
# # # LE CHAMPS username EST OBLIGATOIRE AVEC DJANGO 
# # ON L'IMPLEMENTERA AVEC L'EMAIL DONC LE "email" SERA AUSSI ENREGISTRE DANS "username" 
# # MAIS ON UTILISERA "email" POUR L'IDENTIFICATION DONC UN EMAIL
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
#         if email is not None:
#             instance.email = email
#             instance.username = email
#         if password is not None:
#             instance.set_password(password)

#         instance.save()
#         return instance
    
    

