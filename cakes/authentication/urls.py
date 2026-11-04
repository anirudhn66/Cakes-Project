from django.urls import path

from .views import LoginView

from . import  views

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),

    path('login/',views.LoginView.as_view()),

    path('register/',views.RegisterView.as_view()),

]
