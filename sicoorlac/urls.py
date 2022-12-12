"""sicoorlac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from sicoorlac.views import contacto, inicioAdmin

from django.contrib.auth.views import LoginView as login
from sicoorlac.views import logout_user,contacto,inicioAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.as_view(), name='login'),
    path('logout/', logout_user, name="logout"),
    
    path('adm/',include('administracion.urls')),


    path('entregas/',include('entregas.urls')),
    path('liquidaciones/',include('liquidaciones.urls')),


    path('contacto/', contacto, name="contacto"),
    


]




"""path('admin/bovino',bovino,name='bovinos'),"""

"""path('extras/municipio', municipio, name='municipio')
ver """