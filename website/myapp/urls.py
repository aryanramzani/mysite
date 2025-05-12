
from django.urls import path
from django.urls import include
from myapp import views
urlpatterns = [
    path("home" , views.index_view, name="home"),
    # path("about" , MyView.as_view() , name="about"),
    # path("contact" , MyView.as_view() , name="contact")
]