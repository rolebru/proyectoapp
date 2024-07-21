
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('appcoder/', include("appcoder.urls")) #con esto reconocer urls de la app
]
