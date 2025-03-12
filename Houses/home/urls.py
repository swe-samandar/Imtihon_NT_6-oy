from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    Home,
    HouseDetail,
    HouseCreate,
    HouseUpdate,
    HouseDelete,
    About,
    Contact,
    Index,
    )

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', Home.as_view(), name='home'),
    path('house-detail/<int:pk>/', HouseDetail.as_view(), name='house-detail'),
    path('house-create/', HouseCreate.as_view(), name='house-create'),
    path('house-update/<int:pk>/', HouseUpdate.as_view(), name='house-update'),
    path('house-delete/<int:pk>/', HouseDelete.as_view(), name='house-delete'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)