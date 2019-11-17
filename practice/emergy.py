from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np
import math

# data = read("./data/Xe.wav")
fs, signal = read("./data/khoosoothunhus.wav")


audio = signal
sampsPerMilli = int(fs/1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames  = int(len(signal)/sampsPerFrame)

print('samples/millisecond : %d ' % sampsPerMilli)
print('samples/[%d ms]frame : %d ' % (millisPerFrame,sampsPerFrame))
print('number of frames : %d ' % nFrames)

STEs = []
###### rectangle
# for k in range(nFrames):
#     startIdx = k * sampsPerFrame
#     stopIdx = startIdx + sampsPerFrame
#     window = np.zeros(len(signal))
#     window[startIdx:stopIdx] = 1
#     STE = sum((signal**2)*(window**2))
#     STEs.append(STE)

#### recursive lowpass filter 
fc = 20
a = math.exp(- fc * 2*math.pi /fs)
for n in range(len(signal)):
    if n == 0:
        STEs.append(a*0 + signal[n]**2)
    else:
        STEs.append(a*STEs[n-1] + signal[n] ** 2)

##### short-time zero crossing count
# DC = mean(signal)
# newSignal = signal - DC
# ZCCs = []
# for i in range(nFrames):
#     startIdx = i * sampsPerFrame
#     stopIdx = startIdx + sampsPerFrame
#     s = newSignal[startIdx:stopIdx]
#     ZCC = 0
#     for k in range(1,len(s)):
#         ZCC += 0.5* abs(math.s)


plt.subplot(2, 1, 1)
plt.plot(np.arange(len(signal))/fs,signal)
# plt.title('Short-Time Energy')
plt.ylabel('Amtitude')
# plt.xlabel('FRAME')

plt.subplot(2, 1, 2)
plt.plot(np.arange(len(signal))/fs,STEs)
# plt.title('Short-Time Energy')
plt.ylabel('short-time energy')
# plt.xlabel('FRAME')
plt.show()
# pyplot.autoscale(tight='both')


