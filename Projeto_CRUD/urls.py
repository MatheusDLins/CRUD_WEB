
from django.contrib import admin
from django.urls import path, include
from paginas.api import viewsets as taskviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
