from django.urls import path
# use . to reference urls file in this directory
from .views import homePageView

urlpatterns = [
    path('', homePageView, name="home"),
]
