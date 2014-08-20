import matplotlib as mpl
import numpy as np
import random
mpl.use('Agg')
import matplotlib.pyplot as plt


x_inputs = []
y_inputs = []
diversity = 1
increment = 0.1
def generate_random_input_points():
	for i in np.arange(1,6,increment):
		x_inputs.append(round(i+random.uniform(-diversity,diversity)+1, 2))
		random.seed(i+1)
		y_inputs.append(round(i+random.uniform(-diversity,diversity)+1, 2))		
	# print x_inputs
	# print y_inputs	
generate_random_input_points()	




def draw_graph():
	plt.plot(x_inputs, y_inputs, 'ro') #apparently points
	plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8,], color='1') #draw the line
	plt.axis([0, 8, 0, 8], color='0') 
	plt.savefig('ANN/static/img/graph.png', transparent=True)
	#plt.savefig('graph.png', transparent=True)