import math
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *


def ref_sin_45(t):
	freq   = 2*math.pi/30
	radius = 5

	x     = (math.cos(math.radians(45))*t)-(math.sin(math.radians(45))*radius*math.sin(freq*t))
	y     = (math.sin(math.radians(45))*t)+(math.cos(math.radians(45))*radius*math.sin(freq*t))

	return x,y


def makeFig(): #Create a function that makes our desired plot
	plt.grid(True)
	plt.plot(xrrefary,yrrefary)
	#plt.plot(trrefary,xrrefary)
	#plt.plot(trrefary,yrrefary)



# Store path
xrref = np.array([[0]])
yrref = np.array([[0]])
trref = np.array([[0]])

t = 0
while True:

	x,y = ref_sin_45(t)

	# Store path
	xrref = np.append(xrref, np.array([[x]]), axis=0)
	yrref = np.append(yrref, np.array([[y]]), axis=0)
	trref = np.append(trref, np.array([[t]]), axis=0)
	# Plot
	xrrefary = xrref
	yrrefary = yrref
	trrefary = trref
	drawnow(makeFig)
	plt.pause(.000001)

	t += 1