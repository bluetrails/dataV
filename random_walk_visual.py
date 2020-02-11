import matplotlib.pyplot as plt
from random_walk import RandomWalk


#while True:
#Make a random walk
rw = RandomWalk(50000)
rw.fill_walk()

#Plot the points
plt.style.use('seaborn')
fig,ax = plt.subplots(figsize=(15,7))
point_numbers = range(0,rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_numbers, edgecolors=None, cmap=plt.cm.Blues, s=1)

#emphasize first and last point
ax.scatter(0,0,c='green', s=100, edgecolors=None)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red', s=100,edgecolors=None)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title("A random walk")

plt.show()

    #keep_running  = input('Make another walk ? y/n')
    #if keep_running == 'n':
    #    break