from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

import random
import datetime
from django.utils.timezone import utc

import matplotlib as mpl
import numpy as np
mpl.use('Agg')
import matplotlib.pyplot as plt

from linreg.models import Point
from linreg.linregcore import regression


@csrf_exempt
def linreg(request):
    points = Point.objects.all()
    draw_graph()

    #debug
    #calculate weights
    #ws = regression(points)
    #w0 = ws[1]
    #w1 = ws[0]
    #debug = " w1: " + str(w1) + " w0: " + str(w0)
    return render_to_response('linreg/linreg.html',
                              {
                                  'number_of_inputs' : range(8),
                                  'points' : points,
                                  #'debug' : debug,
                              })
@csrf_exempt
def submit_points(request):
    if request.method == 'POST':
        for input_num in range(8):
            p = Point(id = input_num+1)
            p.posx = float(request.POST.get('x' + str(input_num+1), ''))
            p.posy = float(request.POST.get('y' + str(input_num+1), ''))
            p.save()
    return HttpResponseRedirect('/calculate/')


@csrf_exempt
def randomize_points(request):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    for i in range(8):
        p = Point.objects.get_or_create(id = i + 1)[0]
        random.seed(now.second + i + 8)        
        p.posx = i + round(random.uniform(-1,+1), 2) + 1
        random.seed(now.second + i + 16)
        p.posy = i + round(random.uniform(-1,+1), 2) + 1
        p.save()
    return HttpResponseRedirect('/calculate/')


def draw_graph():
    #points
    mpl.rc('axes', edgecolor="#646d7a")
    mpl.rc('xtick', color="white")
    mpl.rc('ytick', color="white")
    mpl.rc('patch', edgecolor="red")    
    points = Point.objects.all()
    x_inputs = []
    y_inputs = []
    for point in points:
        x_inputs.append(point.posx)
        y_inputs.append(point.posy)
        #print ("x: " + str(x_inputs) + "y: " + str(y_inputs))
    plt.plot(x_inputs, y_inputs, 'go', color="#9ba4ab", markeredgewidth=1,
             markersize=6, marker = '+' # . , + 1 2 3 4
    ) 

    # Temporary test weights
    w0 = 2    
    w1 = 0.7
    
    #calculate weights
    ws = regression(points)
    w0 = ws[1]
    w1 = ws[0]

    # Draw the line
    pts = []
    for i in range(9):
        pts.append(w1*i+w0)
    plt.plot(pts, 'orange') #draw the line
    #alternative way, by (x1, y1, x2, y2)
    #lines = plt.plot(1, 2, 8, 7)
    #plt.setp(lines, color='r', linewidth=2.0)
    
    plt.axis([0, 8, 0, 8])
    plt.plot()    
    plt.savefig('ANN/static/img/graph.png', transparent=True)
    plt.close()

    
@csrf_exempt    
def calculate(request):
    draw_graph()
    return HttpResponseRedirect('/linreg/')    

