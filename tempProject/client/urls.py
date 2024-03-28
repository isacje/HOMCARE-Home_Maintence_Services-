from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('signupUser', views.user_signupUser, name='signupUser'),
	path('signupClient', views.user_signupClient, name='signupClient'),
	path('serviceProvider_signUp',views.serviceProvider_signUp,name='serviceProvider_signUp'),
	path('client_signUpPage',views.client_signUpPage,name='client_signUpPage'),
  	path('signup', views.user_signup, name='signup'),
	path('login', views.user_login, name='login'),
    path('home1', views.user_authenticate, name='authenticate'),
	path('logout', views.user_logout, name='logout'),
]