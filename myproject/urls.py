"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core.views import PostListView, HomeView, apiView, ProductListCreate, ProductRetrieveUpdateDestroy, PostListCreate, PostRetrieveUpdateDestroy
from core.views import ProtectedView, ProtectedJWTView, register_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', apiView.as_view()),
    path('blog/', PostListView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('posts/', PostListCreate.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view()),
    path('protected/', ProtectedView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/protected', ProtectedJWTView.as_view()),
    path('register/', register_user, name="register_user"),
]
