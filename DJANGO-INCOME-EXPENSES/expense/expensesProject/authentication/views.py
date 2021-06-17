from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib import auth

from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse

from .utils import account_activation_token

from django.contrib import auth
# Create your views here.


class EmailValidation(View):
	

	def post(self,request):
		data = json.loads(request.body)
		email = data['email']
		if not validate_email(email):
			return JsonResponse({'email_error':'Email Validation failed'},status=400)
		if User.objects.filter(email=email).exists():
			return JsonResponse({'email_error':'email in use'},status=409)

		return JsonResponse({'email_valid':True})


class UsernameValidation(View):
	def post(self,request):
		data = json.loads(request.body)
		username = data['username']

		if not str(username).isalnum():
			return JsonResponse({'username_error':'username should only contain alphanumeric characters'},status=400)
		
		if User.objects.filter(username=username).exists():
			return JsonResponse({'username_error':'username in use'},status=409)


		return JsonResponse({'username_valid':True})

 

class RegistrationView(View):
	def get(self,request):
		return render(request,'authentication/register.html')

	
	'''
		Function to get the User Input Data 
		from the /authentication/register Page
	'''
	def post(self,request):

		'''Getting User Data'''

		username = request.POST['username']
		email 	 = request.POST['email']
		password = request.POST['password']

		context = {

			'fieldValues':request.POST
		}

		print(username,password,email)

		#messages.success(request,'this is success')
		'''
		messages.warning(request,'this is warning')
		messages.info(request,'this is info')
		messages.error(request,'this is  err')
		'''

		if not User.objects.filter(username=username).exists():
			if not User.objects.filter(email=email).exists():
				if len(password)<6:
					messages.error(request,"password must be greater than 6 characters")
					return render(request,'authentication/register.html',context)

				user=User.objects.create_user(username=username,email=email)
				user.set_password(password)
				'''
				 Making User Activation False
				'''
				user.is_active=False
				user.save()
				
				#path_to_view  for user verification
				
				domain = get_current_site(request).domain

				email_body = {
					'user':user,
					'domain':domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': account_activation_token.make_token(user)
				}

				link = reverse('activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})
				activate_url = 'http://'+domain+link

				email_body = 'Hi '+user.username+' Please use this link to Verify your Account!\n'+activate_url

				email_subject='Acoount Activation Email!!!'
				
				email = EmailMessage(
						email_subject,
						email_body,
						'inbox.dipayan@outlook.com',
						[email],
					)
				email.send(fail_silently=False)
				
				messages.success(request,'Account Suceessfully Created!')
				return render(request,'authentication/register.html')
				
		return render(request,'authentication/register.html')


class VerificationView(View):
	def get(self,request,uidb64,token):

		try:
			id = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=id)

			if not account_activation_token.check_token(user,token):
				return redirect('login'+'?message='+'User already activated')
			if user.is_active:
				return redirect('login')

			user.is_active=True 
			user.save()

			messages.success(request,'Account activated')

			return redirect('login')
			
		except Exception as ex:
			pass 
		return redirect('login')


class LoginView(View):
	def get(self,request):
		return render(request,'authentication/login.html')


	def post(self,request):
		username = request.POST['username']
		password = request.POST['password']

		if username and password:
			user = auth.authenticate(username=username,password=password)

			if user:
				if user.is_active:
					auth.login(request,user)
					messages.success(request,"Successfully Loged in! "+user.username)
					return redirect('expenses')

				messages.error(request,"Acouunt is not Activated ")

				return render(request,'authentication/login.html')
			messages.error(request,'Invalid Credentials!')
			return render(request,'authentication/login.html')

		messages.error(request,'Please all Fields!')
		return render(request,'authentication/login.html')




