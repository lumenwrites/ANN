from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render_to_response('index.html',
		{})
