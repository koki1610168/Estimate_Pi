import numpy as np
import matplotlib.pyplot as plt
import random

###################################################
###############Visualize the Process###############
###################################################


figure, axes = plt.subplots()

axes.set(xlim=(-1, 1), ylim=(-1, 1))
draw_circle = plt.Circle((0, 0), 1.0, fill=False)

axes.set_aspect('equal')
axes.add_artist(draw_circle)

def pi_estimate(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle +=1
            axes.plot(x, y, 'r.')
        else:
            axes.plot(x, y, 'b.')
        num_point_total += 1

    return 4 * num_point_circle / num_point_total
print(pi_estimate(10000))


plt.title('Circle')
plt.show()










