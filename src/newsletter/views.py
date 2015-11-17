from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
	template = 'home.html'
	title = "Welcome"

	form = SignUpForm(request.POST or None)
	context = {
		"template_title" : title,
		"form" : form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
			"template_title" : "Thank You"
		}
	
	return render(request, template, context)
