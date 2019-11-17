from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
from matplotlib import pyplot
import numpy as np 
from scipy import signal
# from scipy.fftpack import fft,ifft

def configFilter(data):
    out = []
    out.append(data[0])
    for i in range(1,len(data)):
        out.append(data[i] - 0.98*data[i-1])
    return out

fs,data = read("../data/Xe.wav")
# print(fs)
# exit()
start = int(0.4*fs)
sizecut = 512

audio = np.array(data)
# audio = data
au = audio[start:start+sizecut]
plt.subplot(3,1,1)
plt.plot(au)
plt.title('original')

audio = configFilter(au)
plt.subplot(3,1,2)
plt.plot(audio)
plt.title('loc hieu chinh')

audio = audio * np.hamming(len(au))
audio = np.abs(np.fft.fft(audio))
maxS = max(audio)
# audio = np.log10(audio/maxS)*(-20)
# audio = np.log10(audio)
audio = audio[0:int(sizecut/2)]
audio = np.fft.ifft(audio)

# plt.subplot(3,1,3)
# plt.plot(audio)
# plt.title('hamming')
# plt.show()

# audio = np.fft.fft(audio)
plt.subplot(3,1,3)
plt.plot(audio)
plt.title('homonophic')


plt.show()

# audio = np.log10(np.abs(audio))
# audio = np.fft.ifft(audio)
# print(audio)

