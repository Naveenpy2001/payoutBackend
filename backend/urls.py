"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

# from app.views import *

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [

#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', ObtainTokenPairWithEmailView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('profile/', ProfileView.as_view(), name='profile'),

#     # update resume CRUD
#     path('profile/resume/', ResumeUpdateAPIView.as_view(), name='update_resume'),
#     # Reusme headline
#     path('profile/resume-headline/', ResumeHeadlineAPIView.as_view(), name='resume_headline'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

