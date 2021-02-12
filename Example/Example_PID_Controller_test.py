import math
import time

# K gain
Kp = 1
Ki = 0
Kd = 0

#Variable PID
Pre_error = 0
Cur_error = 0
Area_old  = 0
Ts = 0.01
time_step = 0


while True:
	V_desired = 5
	tick_count = encoder.get()
	V_current = (2*math.pi*tick_count)/(PPR*Ts)
	Cur_error = V_desired - V_current
	V = Kp*Cur_error + Kd*(Cur_error - Pre_error)/Ts + Ki*(Area_old + Cur_error*Ts)
	Area_old = Area_old + Cur_error*Ts
	Pre_error = Cur_error
	print(f'time step {time_step} : {V}')
	time_step += 1
	time.sleep(0.01)