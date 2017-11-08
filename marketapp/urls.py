from marketapp import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^categories/$', views.CategoryListView.as_view(), name="categories"),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name="category_detail"),
    url(r'^categories/create/$', views.CategoryCreateView.as_view(), name="create_category"),
    url(r'^categories/delete/(?P<pk>\d+)/$', views.CategoryDeleteView.as_view(), name="category_delete"),
    url(r'^carads/$', views.CarAdListView.as_view(), name="carads"),
    url(r'^carads/detail/(?P<pk>\d+)/$', views.CarAdDetailView.as_view(), name="carad"),
    url(r'^carads/(?P<pk>\d+)/$', views.CarAdUpdateView.as_view(), name="carad_update"),
    url(r'^carads/delete/(?P<pk>\d+)/$', views.CarAdDeleteView.as_view(), name="carad_delete"),
    url(r'^carads/create/$', views.CarAdCreateView.as_view(), name="carad_create"),
    url(r'^owners/$', views.OwnerListView.as_view(), name="owners"),
    url(r'^owners/(?P<pk>\d+)/$', views.OwnerUpdateView.as_view(), name="owner_update"),
    url(r'^owners/create/$', views.OwnerCreateView.as_view(), name="owner_create"),
    url(r'^owners/delete/(?P<pk>\d+)/$', views.OwnerDeleteView.as_view(), name="owner_delete"),
    url(r'^owners/detail/(?P<pk>\d+)/$', views.OwnerDetailView.as_view(), name="owner_detail"),
    url(r'^comments/create/$', views.CategoryCreateView.as_view(), name="create_comment")
]