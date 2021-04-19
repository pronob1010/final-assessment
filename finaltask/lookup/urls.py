from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . models import *

urlpatterns = [
    path('', views.index, name="index"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
