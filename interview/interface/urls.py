# interface/urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('dashboard',views.dashboard),
    path('logout',views.logout, name='logout' )
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
