import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import animation

x = [2,5,2]
y = [1,6,7]
figure2 = plt.figure(figsize=(15,10))
ax = plt.subplot(1,1,1)
ax.scatter(x,y ,marker='x',color='red')  # Plot some data on the (implicit) axes.

plt.show()  

def update_scartter(i):
    global x
    global y

    ax.clear()
    # for x in range(3):
    #     x[x] = x[x] + i
    #     y[x] = y[x] + i

    ax.scatter(x,y ,marker='x',color='red')  # Plot some data on the (implicit) axes.


anim = animation.FuncAnimation(figure2, update_scartter, frames = 10, interval = 30)
anim.save('scatter.gif')  