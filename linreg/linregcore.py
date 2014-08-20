from linreg.models import Point
import numpy as np


def w0_update (w1, w0, points):
    learningRate = 0.1
    totalError = 0
    for point in points:
        x = point.posx        
        y = point.posy
        pointError = (y - (w1 * x + w0))
        totalError += pointError
        print "w0 pointError at point " + str(x) + " " + str(y) + " is " + str(pointError)
        print "w0 totalError at point " + str(x) + " " + str(y) + " is " + str(totalError)
        print " "
    return w0 + learningRate*totalError


def w1_update (w1, w0, points):
    learningRate = 0.1
    totalError = 0
    for point in points:
        x = point.posx        
        y = point.posy
        pointError = (y - (w1 * x + w0))*x
        totalError += pointError        
        print "w0 pointError at point " + str(x) + " " + str(y) + " is " + str(pointError)
        print "w0 totalError at point " + str(x) + " " + str(y) + " is " + str(totalError)
        print " "
    return w1 + learningRate*totalError

def regression (points):
    w1 = 0
    w0 = 0
    prev_w1 = - 10    
    prev_w0 = - 10
    learningRate = 0.1
    convergenceThreshold = 0.1
    i = 1

    while i < 3: #((np.square(w1 - prev_w1) > convergenceThreshold) or (np.square(w0 - prev_w0) > convergenceThreshold)):
        print " "
        print "**************** Iteration " + str(i) + " *****************"
        i = i + 1
        
        prev_w1 = w1
        prev_w0 = w0

        w1 = w1_update(w1, w0, points)        
        #w0 = w0_update(w1, w0, points)
        w0 = 1

        print "new w1: " + str(w1)
        print "new w0: " + str(w0)
        print "w0 squared diff: " + str(np.square(w0 - prev_w0))                        

    return [w1, w0]
