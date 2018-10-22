
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


csi_data = pd.read_csv('/home/yao/WIFI_Project/csi_161018_walking.log', sep=';', header = 1,decimal=',', error_bad_lines=False)
csi_data = csi_data.dropna()
i =1
csi_real =[]
csi_img=[]
csi_time =[]
csi_phase =[]
csi_amplitude = []
while i < (csi_data.__len__()):

    csi_time.append(float(csi_data.iloc[i]/1000000))
    csi_real.append(np.int8(csi_data.iloc[i+1]))
    csi_img.append(np.int8(csi_data.iloc[i+2]))
    csi_amplitude.append(math.sqrt(math.pow(np.int8(csi_data.iloc[i+1]),2)+math.pow(np.int8(csi_data.iloc[i+2]),2)))
    csi_phase.append((math.atan2(csi_data.iloc[i+2],csi_data.iloc[i+1]))/math.pi*180)
    i = i+257

#plot
plt.figure(1)
plt.subplot(411)
plt.plot(csi_time,csi_amplitude)
plt.legend(['CSI Amplitude'])
plt.xlabel('in seconds')

plt.subplot(412)
plt.plot(csi_time,csi_real)
plt.legend(['CSI Real in dB'])
plt.xlabel('in seconds')

plt.subplot(413)
plt.plot(csi_time,csi_img)
plt.legend(['CSI Image in dB'])
plt.xlabel('in seconds')

plt.subplot(414)
plt.plot(csi_time,csi_phase)
plt.legend(['CSI Phase'])
plt.xlabel('in seconds')
plt.show()