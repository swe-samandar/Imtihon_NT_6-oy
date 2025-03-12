from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Main, Registration, Dashboard, UserUpdate,login_user, logout_user

urlpatterns = [
    path('main', Main.as_view(), name='main'),
    path('register/', Registration.as_view(), name='register'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user-update/', UserUpdate.as_view(), name='user-update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)