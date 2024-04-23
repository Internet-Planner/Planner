from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib import admin
from .models import User, Planning, Event, Content


class UserAdmin(admin.ModelAdmin):
    ordering = ["email"]
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
        "is_verified",
        "is_certified",
    ]
    list_display_links = ["email"]
    list_filter = [
        "role",
        "is_staff",
        "is_active",
    ]
    search_fields = ["email", "first_name", "last_name", "username"]
    fieldsets = (
        (
            "Login Credentials",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "is_verified",
                    "role",
                )
            },
        ),
        (
            "Important Dates",
            {"fields": ("date_joined", "last_login")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                ),
            },
        ),
    )

# @receiver(post_save, sender=User)
# def create_user_planning(sender, instance, created, **kwargs):
#     if created and not hasattr(instance, 'planning'):
#         Planning.objects.create(user=instance)


class PlanningAdmin(admin.ModelAdmin):
    ordering = ["created_at"]
    model = Planning
    list_display = [
        "user",
        "created_at",
        "updated_at",
        "is_supprime",
    ]
    list_filter = [
        "user",
    ]
    search_fields = ["user"]

    def has_add_permission(self, request):
        return False  # Empêcher l'ajout manuel d'un planning

class ContentInline(admin.StackedInline):
    model = Content
    min_num = 0  # Nombre minimum de formulaires requis, 0 signifie aucun formulaire requis
    extra = 1  # Nombre de formulaires vides à afficher
    can_delete = True  # Permettre la suppression des instances existantes de Content

# class EventAdmin(admin.ModelAdmin):
#     ordering = ["created_at"]
#     model = Event
#     list_display = [
#         "title",
#         "description",
#         "date_start",
#         "date_end",
#         "created_at",
#         "updated_at",
#         "is_supprime",
#     ]
#     fieldsets = (
#         (
#             "Planning",
#             {
#                 "fields": (
#                     "planning",
#                 )
#             },
#         ),
#         (
#             "Event Information",
#             {
#                 "fields": (
#                     "title",
#                     "description",
#                     "date_start",
#                     "date_end",
#                 )
#             },
#         ),
#     )

#     inlines = [ContentInline]  # Ajoute le formulaire pour le modèle Content
  
admin.site.register(User, UserAdmin)
admin.site.register(Planning, PlanningAdmin)
admin.site.register(Event)
