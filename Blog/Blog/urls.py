from django.contrib import admin
from django.urls import path, include
# from Blog.Users.models import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Post/', include('BlogProject.urls')),
    path('api/User/', include('Users.urls'), name="profile"),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
