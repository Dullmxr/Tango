from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),  # This must be here
]
