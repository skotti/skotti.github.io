from django.db import models


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class LoginForm(forms.Form):
 #   username = forms.CharField(label='Username')
  #  password = forms.CharField(label='Password', widget=forms.PasswordInput())

#class UserLoginForm(forms.Form):
 #   username = forms.CharField(label=_(u'Username'), max_length=30)
class BlogPost(models.Model):
	title = models.CharField(max_length = 200)
	item = models.TextField()
	user = models.ForeignKey(User, default = None)

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit = False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user


