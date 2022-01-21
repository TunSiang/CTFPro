from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Component, User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	institution = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ("username","email", "institution", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class componentForm(forms.ModelForm):
	class Meta:
		model = Component
		fields = ["component_id", "Type", "hostname", "url_access", "username",]
		labels = {'component_id': "Component_id", 'Type': "Component Name", 'hostname': "Hostname", 'url_access': "URL", 'username': "Username",}
