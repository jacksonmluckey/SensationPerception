from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('experiment/', include('experiment.urls')),
    path('admin/', admin.site.urls),
]
