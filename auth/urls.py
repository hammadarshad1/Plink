from django.urls import include
from django.conf.urls import url

from auth import views as auth_views

app_name = "auth"

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register/$', auth_views.RegisterView.as_view(), name="register")
]