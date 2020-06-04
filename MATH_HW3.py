import math
def e_slope_function(x, y):
	return y 
def ln_slope_function(x, y):
	return 1/x
def pi_slope_function(x, y):
	return 4/(x*x + 1)
	
def runge_kutta(step, x, y, slope_function):
	k1 = slope_function(x, y)
	#print(k1)
	k2 = slope_function(x+.5*step, y+.5*step*k1)
	#print(k2)
	k3 = slope_function(x+.5*step, y+.5*step*k2)
	#print(k3)
	k4 = slope_function(x+step, y+step*k3)
	#print(k4)
	k_val = (k1 + 2*k2 + 2*k3 + k4)/6.0
	new_y = y + step*k_val
	return new_y

def runge_kutta_to_value(max_val, steps, x, y, slope_function):
	step_val =  (max_val-x) / steps
	step_count = 0
	while step_count < steps:
		y = runge_kutta(step_val, x, y, slope_function)
		x = x + step_val
		step_count += 1
	return y


print("ln answer")
correct_answers_in_row = 0
ln_2 = 0.69314718
n = [10.0, 20.0, 40.0, 80.0, 160.0, 320.0]
runge_kutta_values = []
idx = 0
for val in n:
	val1 = runge_kutta_to_value(2.0, val, 1, 0, ln_slope_function)
	runge_kutta_values.append(val1)
	idx += 1

idx = 10	
for answer in runge_kutta_values:
	#print(answer)
	#print(abs(answer - ln_2))
	if abs(answer - ln_2) < 0.00000001:
		print(answer)
		print(idx)
		correct_answers_in_row+=1
		if correct_answers_in_row > 1:
			break
	idx = idx*2


print("pi answer")
correct_answers_in_row = 0
pi = 3.141592653589793
n = [10.0, 20.0, 40.0, 80.0, 160.0, 320.0]
runge_kutta_values = []
idx = 0
for val in n:
	val1 = runge_kutta_to_value(1.0, val, 0, 0, pi_slope_function)
	runge_kutta_values.append(val1)
	idx += 1

idx = 10	
for answer in runge_kutta_values:
	#print(answer)
	#print(abs(answer - ln_2))
	if abs(answer - pi) < 0.00000001:
		print(answer)
		print(idx)
		correct_answers_in_row+=1
		if correct_answers_in_row > 1:
			break
	idx = idx*2