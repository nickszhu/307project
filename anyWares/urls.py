from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^itemView/(?P<item_id>[0-9]+)/$', views.itemView, name='itemView'),
    url(r'^signup/$', views.signup, name='signup'),
]