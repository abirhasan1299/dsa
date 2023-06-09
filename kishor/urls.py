from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kobita/', include('kobita.urls')),
    path('',home,name="Home"),
    path('post/<int:pk>/',view_page,name="Post"),
    path('form/',sendUs,name="Form")
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
