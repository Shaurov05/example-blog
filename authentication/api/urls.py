from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from authentication.api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserRegistrationView)

urlpatterns = [

    # APIView
    path('users/<pk>/', UserUDRView.as_view(), name='article-detail'),
    path('', include(router.urls)),

    # login and logout url
    path('login/', UserLoginView.as_view(), name='login_api'),
    path("current/user/", CurrentUserAPIView.as_view(), name='current-user'),
]
