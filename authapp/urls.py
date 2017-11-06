from . import views
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

urlpatterns = [

    url(r'^signup/$', views.SignUpCreateView.as_view()),
    url(r'^signin/$', views.MyLoginView.as_view()),
    url(r'^signout/$', LogoutView.as_view(), name="signout"),
]