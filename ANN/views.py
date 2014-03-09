from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

def main(request):
    return render_to_response('index.html')
