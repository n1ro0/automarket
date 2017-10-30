"""automarketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from marketapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^categories/$', views.CategoryListView.as_view(), name="categories"),
    url(r'^categories/detail/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name="category_detail"),
    url(r'^carads/$', views.CarAdListView.as_view(), name="carads"),
    url(r'^carads/detail/(?P<pk>\d+)/$', views.CarAdDetailView.as_view(), name="carad"),
    url(r'^carads/(?P<pk>\d+)/$', views.CarAdUpdateView.as_view(), name="carad_update"),
    url(r'^carads/delete/(?P<pk>\d+)/$', views.CarAdDeleteView.as_view(), name="carad_delete"),
    url(r'^carads/create/$', views.CarAdCreateView.as_view(), name="carad_create"),
    url(r'^owners/$', views.OwnerListView.as_view(), name="owners"),
    url(r'^owners/(?P<pk>\d+)/$', views.OwnerUpdateView.as_view(), name="owner_update"),
    url(r'^categories/create/$', views.CategoryCreateView.as_view(), name="create_category"),
    url(r'^comments/create/$', views.CategoryCreateView.as_view(), name="create_comment")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

