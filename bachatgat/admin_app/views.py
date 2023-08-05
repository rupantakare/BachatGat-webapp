from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def admin_app(request):
    template = loader.get_template('firstpage.html')
    return HttpResponse(template.render)

#def admin_app(request):
 #   return HttpResponse("Hello world!")