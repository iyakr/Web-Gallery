from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf.urls import include

# router = DefaultRouter()
# router.register('users/', UserViewSet)

urlpatterns = [
    path('', ProfileUser.as_view()),
    path('update-ava/<int:pk>/', UpdateProfile.as_view()),
    # path('update-ava/', ImageView.as_view()),
    # url(r'^upload/(?P<filename>[^/]+)$', UpdateProfile.as_view()),
    path('reg2/', RegUser.as_view()),
    # path('reg2/', CreateUserAPIView.as_view()),
    path('red/<int:pk>/', RedactProfile.as_view()),
]
