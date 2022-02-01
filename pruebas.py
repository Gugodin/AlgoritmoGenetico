import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import animation

x = [2,5,2]
y = [1,6,7]

figure2 = plt.figure(figsize=(15,10))
ax = plt.subplot(1,1,1)
ax.scatter(x,y ,marker='x',color='red')  # Plot some data on the (implicit) axes.
    
plt.show()

def generarGraficas():
    for i in range(3):
        figure2 = plt.figure(figsize=(15,10))
        ax = plt.subplot(1,1,1)
        ax.plot(5,5 ,marker='x',color='red',lw = 0)  # Plot some data on the (implicit) axes.
        ax.plot(10,2 ,marker='x',color='red',lw = 0)  # Plot some data on the (implicit) axes.
        
        plt.savefig(f'./prue/img{i}')

        plt.show()  



generarGraficas()



