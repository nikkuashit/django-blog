from django.urls import path
from . import views
urlpatterns = [
    # path('hello/', views.helloWorld),
    path('', views.landingPage, name="home"),
    path('create/', views.createBlog, name="create")

]
