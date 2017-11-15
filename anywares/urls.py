from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /anywares/
    url(r'^$', views.index, name='index'),
    # ex: /anywares/ry511/
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
]