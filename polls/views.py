from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from models import MyRegistrationForm
from models import BlogPost
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import logout

#from polls.models import LoginForm


def index(request):
	#form = LoginForm()
	#if ('username' in request.REQUEST) and ('password' in request.REQUEST):
	#	username = request.REQUEST['username']
	#	password = request.REQUEST['password']
	#	user = authenticate(username=username, password=password)
	#	print(user)
	return render(request, 'polls/index.html')

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			subject = 'blabla'
			message = 'hi'
			from_email = 'NatashaRuzh@yandex.ru'
			to_list = [new_user.email, 'NatashaRuzh@yandex.ru']
			send_mail(subject, message, from_email, to_list, fail_silently = True)
		return HttpResponseRedirect("/polls/")
	else:
		form = MyRegistrationForm()
		return render(request, 'polls/register.html', {'form':form})

@login_required
def post_show(request):
	if ('title' in request.REQUEST) and ('item' in request.REQUEST):
		title = request.REQUEST['title']
		item = request.REQUEST['item']
		BlogPost(title=title, item=item, user=request.user).save()
	return render(request, 'polls/post_show.html')


def logout_view(request):
    logout(request)
    return redirect('/polls/')


## username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)
    #if user is not None:
     #   if user.is_active:
     #       login(request, user)
            # Redirect to a success page.
      #  else:
       # 	raise Http404
            # Return a 'disabled account' error message
    #else:
    	#raise Http404
        # Return an 'invalid login' error message.

# Create your views here.
