from django.contrib import admin
from django.urls import path
from api.views import home, services, add_service

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', home),
    path('api/services/', services),
    path('api/add-service/', add_service),
]