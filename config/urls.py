"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
# from django.urls import path
from django.urls import path, include
from mysite import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('blog/', include('blog.urls')),
    path('signup/', views.signup),
    # path('mypage/', views.mypage),
    path('mypage/', views.MypageView.as_view()),
    # path('contact/', views.contact),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),
    # view単位 DBキャッシュ
    path('cache_test/', views.cache_test),
    # url単位 DBキャッシュ
    path('cache_test2/', cache_page(10)(views.cache_test2)),
    # templateキャッシュ
    path('cache_test3/', views.cache_test3),
]
