import scipy as scp 
from scipy import signal 
from scipy.fftpack import fft,ifft
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io.wavfile import read 

rate,data = read('../data/Xe.wav')

N = 300
K = 1000

data = np.array(data)
audio = []
for d in data:
    if abs(d)>12000:
        audio.append(d)
    else:
        audio.append(0)
    # audio.append(d if abs(d)>10000 else 0)

# autocorrelation
def R(dat):
    out = []
    for i in range(K):
        rK = 0
        for j in range(len(dat)-i-1):
            rK += dat[j]*dat[j+i]
        out.append(rK)
    return out

d = R(audio[5000:7000])
plt.plot(d)
plt.show()


