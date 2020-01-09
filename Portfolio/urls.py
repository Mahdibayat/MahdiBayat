from django.conf.urls import url
from . import views

app_name = 'Portfolio'

urlpatterns = [
    url(r'^/', views.index)
]
