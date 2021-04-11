# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files

    # path('', views.redirect_to_login),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('welcome/', views.login_view),
    # path('create-account/', views.create_account_view),
    # path('home/', views.dashboard_view),
    # path('account-management/', views.account_management_view)
]
