
from django.urls import path
from django.urls import include
from myapp.views import index_view , contact_view , about_view
urlpatterns = [
    path("" , index_view, name="home"),
    path("about" , about_view , name="about"),
    path("contact" , contact_view , name="contact")
]