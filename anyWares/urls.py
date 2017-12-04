from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^itemview$', views.itemView, name='itemView'),
    url(r'^createItem/$', views.createItem, name='createItem'),
    url(r'^itemView/$', views.itemView, name='itemView'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/anyWares/'}),
    url(r'^account/$', views.account, name='account'),
    url(r'^about$', views.about, name="about"),
    url(r'^myitems$', views.myitems, name="myitems"),
    url(r'^edititem/$', views.edititem, name="edititem")
]