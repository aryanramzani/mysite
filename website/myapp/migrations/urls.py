
from django.urls import path
from website.views import index

urlpatterns = [

    path("home" , index.view),
    path("about" , about.view),
    path("contact" , about.contact)
]
