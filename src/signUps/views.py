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
from django.db import IntegrityError


# Create your views here.

def home(request):

	
	# Registration form instance
	#form = SignUpForm(request.POST or None)


	#Booleans/strings used mainly in html to check if form is valid
	requestType = request.POST.get('action',False)
	notMatched = False
	passwordMatch = True
	allFieldsCompleted = True
	usernameTaken = False
	username = ''
	password = ''
	email = ''
	firstName = ''
	lastName = ''
	#user = ''
	
	#Checks if registration submit
	if(requestType == "Register"):

		#logouts out any currentlly logged in user
		#auth.logout(request)

		#Gets all info from HTML using POST and puts in local variable
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		email = request.POST.get('email','')
		firstName = request.POST.get('first_name', '')
		lastName = request.POST.get('last_name', '')
		repassword = request.POST.get('reenter','')
		
		#Checks to see if all fields on registration form are completed
		if(username == '' or password == '' or email == '' or firstName == '' or lastName == '' or repassword == ''):
			allFieldsCompleted = False

		#Checks to see if SignUpForm is valid following models created
		if(allFieldsCompleted == True):
			
			allFieldsCompleted = True
			notMatched = False
			passwordMatch = True

			#If password doesn't equal re-enter field then returns same SignUp.html page
			if(password != repassword):
				passwordMatch = False
				return render(request,"SignUp.html",locals())

			#Tries to create an user
			try:
				user = User.objects.create_user(username,email,password)
				user.first_name = firstName
				user.last_name = lastName
				user.save()
			except IntegrityError:
				#Fails if username already taken so sends this message 
				usernameTaken = True
				return render(request,"SignUp.html",locals())


			usernameTaken = False

			#Sends confirmation email to user who signed up
			subject = 'Thank you for singing up with engineersarecreative!'
			message = 'Welcome to engineersarecreative! Please try out our beta version of the site and give us advice on how to improve.'
			from_email = settings.EMAIL_HOST_USER
			to_list = [email, settings.EMAIL_HOST_USER]
			send_mail(subject,message,from_email,to_list,fail_silently = True)

			#If registration successful outputs this message
			messages.success(request,"We will be in touch")
			#return HttpResponseRedirect('/thank-you/')
			return render(request, "thankyou.html", locals())
		

    #Checks if login submit
	elif(requestType == "Login"):

		#Get username and password from html using POST
		#auth.logout(request)
		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		#Makes sure they are in the database
		user = None
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			#Login user if user is valid
			auth.login(request,user)
			settings.CHECK = True
			#return render(request, "login.html", locals())
			#return HttpResponse("Welcome" + " " + user.username)
		else:
			#Else outputs error message
			notMatched = True
	elif(requestType == "logout"):
		auth.logout(request)
		settings.CHECK = False

	if(request.user.is_authenticated() or settings.CHECK == True):
		return render(request,"login.html",locals())
	else:
		return render(request,"SignUp.html",locals())

#Output thank you page after registration is successful
def thankyou(request):
	notMatched = False
	requestType = request.POST.get('action',False)

	if(requestType == "Login"):

		#Get username and password from html using POST
		#auth.logout(request)
		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		#Makes sure they are in the database
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			#Login user if user is valid
			auth.login(request,user)
			#return HttpResponse("Welcome" + " " + user.username)
			return render(request,"login.html",locals())
		else:
			#Else outputs error message
			notMatched = True
	return render(request,"thankyou.html",locals())



    