from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np
from numpy.fft import fft, fftshift

data = read("./data/Xe.wav")
audio = data[1]

au = []
k = 1000

a = []
for i in range(len(audio)):
    if abs(audio[i]) < 11000:
        a.append(float(0))
    else:
        a.append(audio[i])

a = np.array(a)
# print(len(a))
for idx in range(k):
    r = 0
    for i in range(2000-k):
        r += a[5000+i]*a[5000+i+idx]
    au.append(r)

print(len(au))

plt.plot(au)
plt.show()

