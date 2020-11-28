from django.contrib import admin
from django.urls import path, include
from dashboard.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls'))
]
