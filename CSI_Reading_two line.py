import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import math

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(1000))
line2, = ax.plot(np.random.rand(1000))
ax.set_ylim(0, 80)
xdata, ydata,zdata = [0]*1000, [0]*1000, [0]*1000
raw = serial.Serial("/dev/ttyUSB0",115200)

def update(data):
    line.set_ydata(data)

    return line,


def run(data):
    t,y,z = data
    del xdata[0]
    del ydata[0]
    del zdata[0]
    xdata.append(t)
    ydata.append(y)
    zdata.append(z)

    line.set_data(xdata, ydata)
    line2.set_data(xdata,zdata)
    return line,

def data_gen():
    t = 0
    amplitude =0
    
    while True:
        t+=1
        if (t==1000):
            t = 0

        try:

            real = np.int8(raw.readline())
            imag = np.int8(raw.readline())
            amplitude = math.sqrt(pow(real,2)+pow(imag,2))

        except:
            dat = 0

        yield t, amplitude


ani = animation.FuncAnimation(fig, run, data_gen, interval=0, blit=True)

plt.grid(True)
plt.show()