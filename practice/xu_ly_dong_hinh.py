from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np
import math

fs, signal = read("./data/Xe.wav")

au = []
k = 1000

a = signal
a = np.array(a)
a = a[5000:12000]
a = np.hamming(len(a))*a

a = np.fft.fft(a)
a = np.log(a)
a = np.fft.ifft(a)

plt.plot(a)
plt.show()