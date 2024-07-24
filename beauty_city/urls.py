"""
URL configuration for beauty_city project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static

from beautycity_app import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('administrator', views.administrator, name='administrator'),
    path('notes', views.notes, name='notes'),
    path('popup', views.popup, name='popup'),  # Сделано для пред просмотра
    path('service', views.service, name='service'),
    path('', include('accounts.urls', namespace='accounts')),
    path('service_finally', views.service_finally, name='service_finally'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
