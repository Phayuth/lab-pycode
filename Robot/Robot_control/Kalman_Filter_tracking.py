import numpy as np
from drawnow import *
import time
import matplotlib.pyplot as plt
import math
import random

def makeFig(): # For drawnow function
	plt.plot(x_store,y_store)
	plt.grid(True)

def circle_func(t):
	freq   = 2*math.pi/30

	x = 5*math.cos(freq*t)
	y = 5*math.sin(freq*t)

	return x,y

def kalman_ori(x,y,theta,v,w,P):
	pass



x_store = np.empty([1,1])
y_store = np.empty([1,1])
t_store = np.empty([1,1])

t=0
while True:
	x,y = circle_func(t)
	x = x+random.random()
	y = y+random.random()
	x_store = np.append(x_store,np.array([[x]]), axis=0)
	y_store = np.append(y_store,np.array([[y]]), axis=0)
	t_store = np.append(t_store,np.array([[t]]), axis=0)
	if t>100:
		x_store = np.delete(x_store, 0, 0)
		y_store = np.delete(y_store, 0, 0)
		t_store = np.delete(t_store, 0, 0)
	drawnow(makeFig)
	plt.pause(.000001)
	t+=1