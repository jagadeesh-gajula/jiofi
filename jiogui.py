import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.gcf()
fig.show()
fig.canvas.draw()

for i in range(300):
    # compute something
    plt.plot([1], [2]) # plot something
    
    # update canvas immediately
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    #plt.pause(0.01)  # I ain't needed!!!
    fig.canvas.draw()