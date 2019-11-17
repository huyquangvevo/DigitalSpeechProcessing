from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np

data = read("./data/Xe.wav")

audio = data[1]

N = 1000
n= 5000

K = 500

D = []
au = []

for a in audio:
    if a <11000:
        au.append(0)
    else:
        au.append(a)
audio = np.array(au)
for k in range(K):
    for au in range(N):
        D.append(abs(audio[n+au] - audio[n+au-k])) 

# plt.plot(np.arange(len(audio))/data[0], audio)
# plt.plot(D)
# plt.plot(audio)
plt.ylabel("Ampitude")
plt.xlabel("Time(ms)")

plt.title("Sample wav")
plt.show()