# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, welcome_view, intro_view, people_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    #added paths
    path('welcome/', welcome_view, name='welcome'),
    path("proj_intro/", intro_view, name="intro"),
    path("people/", people_view, name="people"),
    #path("analytics/", analytics_view, name="google-visulizer"),



]
