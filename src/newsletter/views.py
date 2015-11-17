from django.shortcuts import render

# Create your views here.

def home(request):
	template = 'home.html'
	title = "My Title %s" % (request.user)
	context = {
		"template_title" : title,
	}
	return render(request, template, context)
