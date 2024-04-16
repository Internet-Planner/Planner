from django.urls import path
from backend.api import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.register, name='register'), 
    path('activate/<uidb64>/<token>/', views.activate, name='activate_account'), 

    path('forgot-password/', views.forgotPassword, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.resetPassword, name='reset_password'),
]
