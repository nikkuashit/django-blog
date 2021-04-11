from django.urls import path, include
from . import views

urlpatterns = [
    # path('hello/', views.helloWorld),
    path('signup', views.signUp, name="signup"),
    path('signin', views.signIn, name="signin"),
    path('blog/', include("blog.urls")),
]
