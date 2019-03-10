import random
import math
def MonteCarlo(f, g, x0, x1, y0, y1, n):
	f_mean = 0          
	num_inside = 0      
	for t in range(n):
		x = random.uniform(x0, x1)
		y = random.uniform(y0, y1)
		if( g(x, y) == True):
			num_inside += 1
			f_mean += f(x, y)
	f_mean = f_mean/num_inside
	area = num_inside/n*(x1 - x0)*(y1 - y0)
	return area*f_mean

g = lambda x, y: (True if (0 <= x <= math.pi) and (x <= y <= math.pi) else False) 

x0 = 0; x1 = math.pi; y0 = 0; y1 = math.pi
n=38416
value_calculated_w_MMC = MonteCarlo( lambda x, y: (math.cos(x + y)), g, x0, x1, y0, y1, n)
value_trully = -2
print(value_calculated_w_MMC)
