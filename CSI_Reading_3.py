import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque

import matplotlib.pyplot as plt 
import matplotlib.animation as animation


# plot class
class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 115200)


      self.ay = deque([0.0]*maxLen)
      self.maxLen = maxLen

  # add to buffer
  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
      else:
          buf.pop()
          buf.appendleft(val)

  # add data
  def add(self, data):


      self.addToBuf(self.ay, data)

  # update plot
  def update(self, frameNum, a0, a1):
      try:
          line = self.ser.readline()
          data = np.int8(line)
          print(data)
          line2 = self.ser.readline()
          imag =np.int8(line2)
          # print data
          self.add(data)
          a1.set_data(range(self.maxLen), self.ay)
      except KeyboardInterrupt:
          print('exiting')

      return a0, 

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    

# main() function
def main():


  #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = "/dev/ttyUSB0"

  print('reading from serial port %s...' % strPort)

  # plot parameters
  analogPlot = AnalogPlot(strPort, 1000)

  print('plotting data...')

  # set up animation
  fig = plt.figure()
  ax = plt.axes(xlim=(0, 1000), ylim=(-100, 100))
  a0, = ax.plot([], [])
  a1, = ax.plot([], [])
  anim = animation.FuncAnimation(fig, analogPlot.update, 
                                 fargs=(a0, a1), 
                                 interval=50)

  # show plot
  plt.show()

  # clean up
  analogPlot.close()

  print('exiting.')


# call main
if __name__ == '__main__':
  main()