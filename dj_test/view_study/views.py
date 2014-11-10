from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

def hello(request):
	name = "saaru"
	return render_to_response('hello.html' , {'name' : name})

def hello_legacy(request):
	name = "saravana"
	t=get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html)

def simple_hello(request):
	name = "Saro"
	html = "<html><body> Hi %s <br> Welcome to the django vintage club </html></body>" %name
	return HttpResponse(html)

class HelloTemplate(TemplateView):
	template_name = "hello.html"
	
	def get_context_data(self,**kwargs):
		context = super(HelloTemplate,self).get_context_data(**kwargs)
		context['name'] = "Saravanan"
		return context	
		