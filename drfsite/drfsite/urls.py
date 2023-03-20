"""drfsite URL Configuration

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
from django.urls import path, include, re_path

from women.views import *
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



# Урок 9: Роутеры: SipleRouter и DefaultRouter

# router = routers.SimpleRouter() # Отсутствует путь 127.0.0.1:8000/api/v1/
# router.register(r'women', WomenViewSet)

# router = routers.DefaultRouter() # Присутствует путь 127.0.0.1:8000/api/v1/
# router.register(r'women', WomenViewSet, basename="women")

# class MyCustomRouter(routers.SimpleRouter):
#     """
#     Пример собственного роутера
#     """
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'}),
#     ]
# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename="women")



urlpatterns = [
    path("admin/", admin.site.urls),

    # path("api/v1/womenlist/", WomenAPIList.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIUpdate.as_view()),
    # path("api/v1/womendetail/<int:pk>/", WomenAPIDetailView.as_view()),

    # path('api/v1/', include(router.urls)), # http:/127.0.0.1:8000/api/v1/women

    path("api/v1/women/", WomenAPIList.as_view()),
    path("api/v1/women/<int:pk>/", WomenAPIUpdate.as_view()),
    path("api/v1/womendelete/<int:pk>/", WomenAPIDestroy.as_view()),

    # Урок 11: Авторизация и аутентификация. Session-based authentication
    path("api/v1/drf-auth/", include("rest_framework.urls")),

    # Урок 12: Аутентификация по токенам. Пакет Djoser (поддерживает регистрацию, авторизацию и т.д.)
    path("api/v1/auth/", include('djoser.urls')),
    re_path(r"^auth/", include('djoser.urls.authtoken')),

    # Урок 14: Авторизация по JWT-токенам
    path("api/v1/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name='token_verify'),
]
