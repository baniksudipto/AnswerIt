from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/' , views.index , name='index'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    url(r'^(?P<id>\d+)/$', views.user),
    url(r'^detail/(?P<id>\d+)/$', views.User_detail),

]
