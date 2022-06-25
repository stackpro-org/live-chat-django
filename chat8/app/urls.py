
from django.urls import path
from . import views
urlpatterns = [
    # group_name = url>views>index.html>routing>consumer
    path('chat/', views.home),
    path('<str:group_name>/', views.index, name="group_name"),

    path('', views.live_chat),
]
