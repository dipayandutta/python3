from .views import RegistrationView,UsernameValidation,EmailValidation,VerificationView,LoginView,LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect

urlpatterns = [
	path('register',RegistrationView.as_view(),name='register'),
	path('validate-username',csrf_exempt(UsernameValidation.as_view()),name='validate-username'),
	path('validate-email',csrf_exempt(EmailValidation.as_view()),name='validate-email'),
	path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'),
	path('login',LoginView.as_view(),name='login'),
	path('logout',LogoutView.as_view(),name='logout'),
]