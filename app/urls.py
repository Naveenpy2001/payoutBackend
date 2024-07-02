from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app.views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainTokenPairWithEmailView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # update resume CRUD
    path('profile/resume/', ResumeUpdateAPIView.as_view(), name='update_resume'),
    # Reusme headline
    path('profile/resume-headline/', ResumeHeadlineAPIView.as_view(), name='resume_headline'),
]