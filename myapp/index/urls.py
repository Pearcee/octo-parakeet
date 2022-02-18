from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_index, name="index_index"),
    path("index", views.index_index, name="index_index"),
    path("about/", views.index_about, name="index_about"),
    path("contact", views.index_contact, name="index_contact"),
    path("home", views.index_home, name="index_home"),
    path("links", views.index_links, name="index_links"),
    path("location", views.index_location, name="index_location"),
    path("server", views.index_server, name="index_server"),
    path("clock", views.index_clock, name="index_clock"),
]