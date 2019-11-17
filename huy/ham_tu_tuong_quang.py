from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
from matplotlib import pyplot
import numpy as np
import math

fs, signal = read("../data/Xe.wav")
# s = signal[5000:10000]
### autocorrelation
# s = np.asarray(s) 
s = signal
audio = []
for i,a in enumerate(s):
    sample = float(a) if abs(a) > 11000 else float(0)
    audio.append(sample)

s = np.array(audio)
# s = audio[5000:10000]
print(s)
print(len(s))
au = []
N = 300
K = 1000
for k in range(K):
    phi = 0
    for n in range(0, 2000 - K):
        phi += s[5000+n]*s[5000+n+k]
    au.append(phi)


plt.subplot(2, 1, 1)
plt.plot(signal)
plt.title('Original')
plt.ylabel('Signal')
plt.xlabel('signal')

plt.subplot(2, 1, 2)
plt.plot(au)
# plt.title('Short-Time Energy')
plt.ylabel('autocorrelation')
plt.xlabel('signal')
plt.show()
# # pyplot.autoscale(tight='both')


