from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import SignUpForm
from .forms import LoginForm
from django.core.context_processors import csrf
from django.contrib import auth
from .models import signUp
from django.contrib.auth.models import User

# Create your views here.
def home(request):

	form = SignUpForm(request.POST or None)

	requestType = request.POST.get('action',False)
	notMatched = False
	allFieldsCompleted = True
	username = ''
	password = ''
	email = ''
	firstName = ''
	lastName = ''
	
	if(requestType == "Register"):
		
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		email = request.POST.get('email','')
		firstName = request.POST.get('first_name', '')
		lastName = request.POST.get('last_name', '')

		if(username == '' or password == '' or email == '' or firstName == '' or lastName == ''):
				allFieldsCompleted = False

		if form.is_valid():
			save_it = form.save(commit = False)
			save_it.save()
			allFieldsCompleted = True
			notMatched = False

			user = User.objects.create_user(username,email,password)
			user.first_name = firstName
			user.last_name = lastName
			user.save()

			subject = 'Thank you for singing up with engineersarecreative!'
			message = 'Welcome to engineersarecreative! Please try out our beta version of the site and give us advice on how to improve.'
			from_email = settings.EMAIL_HOST_USER
			to_list = [save_it.email, settings.EMAIL_HOST_USER]
			send_mail(subject,message,from_email,to_list,fail_silently = True)

			messages.success(request,"We will be in touch")
			return HttpResponseRedirect('/thank-you/')
		


	elif(requestType == "Login"):

		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request,user)
			return HttpResponse("Welcome" + " " + user.username)
		else:
			notMatched = True
			#return HttpResponse('Invalid')

	return render_to_response("SignUp.html",locals(),context_instance = RequestContext(request))

def thankyou(request):
	notMatched = False
	return render_to_response("thankyou.html",locals(),context_instance = RequestContext(request))



    