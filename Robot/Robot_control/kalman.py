import numpy as np
from drawnow import *
import time
import matplotlib.pyplot as plt
import math
import random

def makeFig(): # For drawnow function
	plt.plot(tt,yy)

def sin_func(t):
	freq   = 2*math.pi/30

	y = 5*math.sin(freq*t)

	return y

def kalman_ori(x,y,theta,v,w,P):
	pass
	# A        = np.array([1,0,0],[0,1,0],[0,0,1])
	# B        = np.array([1,0],[0,1],[1,1])
	# state    = np.array([x],[y],[theta])
	# u        = np.array([v],[w])
	# state_pre= A @ state + B @ u
	# P_pre    = state @ P @ np.transpose(state_pre) +
def kalman_ext():
	pass
def kalman_ust():
	pass

yy = np.array([[0]])
tt = np.array([[0]])
t = 0
while True:
	y = sin_func(t)+random.random()
	yy = np.append(yy,np.array([[y]]),axis=0)
	tt = np.append(tt,np.array([[t]]),axis=0)
	if t>100:
		yy = np.delete(yy, 0, 0)
		tt = np.delete(tt, 0, 0)
	drawnow(makeFig)
	plt.pause(.000001)
	t+=1