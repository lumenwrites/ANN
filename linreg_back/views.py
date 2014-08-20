from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from linreg.models import Point

from django.views.decorators.csrf import csrf_exempt

#import linreg.drawGraph


@csrf_exempt
def linreg(request):
    
    #draw_graph()
    return render_to_response('linreg/linreg.html',
                              {
                                  'values' : request.POST.get('1-0', ''),
                                  'number_of_inputs' : range(8),
                              })
@csrf_exempt
def submit_points(request):
    if request.method == 'POST':
        for input_num in range(8):
	        p = Point(input_number = fromPOST,
                          posx = request.POST.get(str('x'+input_num), ''),
                          posy = request.POST.get(str('x'+input_num), ''))
                p.save()
    return HttpResponseRedirect('/linreg/')
