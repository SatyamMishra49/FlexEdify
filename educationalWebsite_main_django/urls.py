"""
URL configuration for educationalWebsite_main_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, reverse_lazy
from educationalWebsite_main_django import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name='login'),
    path('',views.home,name='home'),
    path('profile/',views.profile, name='profile'),
    path('games/',views.games,name='games'),
    path('geminiai.html', views.geminiai, name='geminiai'),
    path('mathlearning/', views.mathlearning, name='mathlearn'),
    path('mathlearning/<str:chapter>/', views.mathchaplearning, name='mathlearning'),
    path('mathlearning/<str:chapter>/adaptivelearning/', views.tryingaritm, name='mathadaptivelearning'),
    path('mathlearning/<str:chapter>/adaptivelearning/test/', views.test, name='mathtest'),
    path('mathlearning/<str:chapter>/subtopiclearn', views.subtopiclearn, name='mathsubtopiclearn'),
    path('sciencelearning/', views.sciencelearning, name='sciencelearn'),
    path('sciencelearning/<str:chapter>/', views.sciencechaplearning, name='sciencelearning'),
    path('sciencelearning/<str:chapter>/adaptivelearning/', views.tryingaritm, name='scienceadaptivelearning'),
    path('sciencelearning/<str:chapter>/adaptivelearning/test/', views.test, name='sciencetest'),
    path('sciencelearning/<str:chapter>/subtopiclearn', views.subtopiclearn, name='sciencesubtopiclearn'),
]
