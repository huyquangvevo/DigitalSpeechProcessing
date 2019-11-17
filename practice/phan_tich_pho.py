from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np
from numpy.fft import fft, fftshift, ifft

data = read("./data/Xe.wav")
# print(data[1])
audio = data[1]
# print()

au = []

for idx in range(len(audio)):
    if idx > 0:
        au.append(audio[idx] - 0.96*au[len(au)-1])
    else:
        au.append(audio[idx])

audio = au
audio = audio[:512]*np.hamming(512)

audio = fft(audio)
audio = np.log2(np.abs(audio))

audio = ifft(audio)

plt.plot(audio)
# plt.ylabel("Ampitude")
# plt.xlabel("Time(ms)")

plt.title("Sample wav")
plt.show()