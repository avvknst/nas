import math
x = 0.5
a = 0.05
b = 0.7
y = (x**2 * (x+1))/(b - math.sin(x+a)**2 )

print(f"y = {y}")