from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
]
