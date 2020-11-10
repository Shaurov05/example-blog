from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from authentication.api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserRegistrationView)

urlpatterns = [

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('hello/', HelloView.as_view(), name='hello'),

    # APIView
    # path('users/', UserRegistrationView.as_view(), name='article-list'),
    path('users/<pk>/', UserUDRView.as_view(), name='article-detail'),


    # path('register/', UserRegistrationView.as_view(), name='api_register'),
    path('', include(router.urls)),

]
