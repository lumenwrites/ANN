from django.conf.urls import *
#from linreg.models import *

urlpatterns = patterns('',
                       url(r'^linreg/', 'linreg.views.linreg'),
                       url(r'^submit-points/', 'linreg.views.submit_points'),
)
