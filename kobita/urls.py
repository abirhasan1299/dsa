from django.urls import path
from .views import *

urlpatterns = [
    path("<uuid:ud>/",kobita_home,name="kobita"),
    path("logout/",logout,name="logout"),
    path("signup/",signup,name="signup"),
]
