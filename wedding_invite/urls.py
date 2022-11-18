"""wedding_invite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from invite.views import get_invite, get_sign_in, register_request, logout_request, password_reset_request  # noqa
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', get_sign_in, name='get_sign_in'),
    path('invite/<user_id>', get_invite, name='get_invite'),
    path("register/", register_request, name="register"),
    path("logout", logout_request, name="logout"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='invite/password/password_reset_done.html'), name='password_reset_done'),  # noqa
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="invite/password/password_reset_confirm.html"), name='password_reset_confirm'),  # noqa
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='invite/password/password_reset_complete.html'), name='password_reset_complete'),  # noqa
    path("password_reset", password_reset_request, name="password_reset")
]
