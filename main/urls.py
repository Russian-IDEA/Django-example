from django.urls import path
from .views import home, login_page, logout_page, signup_page, add, post

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_page, name='signup'),
    path('add/', add, name='add'),
    path('post/', post, name='post'),
]