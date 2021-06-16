from .views import RegistrationView,UsernameValidation,EmailValidation
from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect

urlpatterns = [
	path('register',RegistrationView.as_view(),name='register'),
	path('validate-username',csrf_exempt(UsernameValidation.as_view()),name='validate-username'),
	path('validate-email',csrf_exempt(EmailValidation.as_view()),name='validate-email'),

]