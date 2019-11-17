from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

fs,data = wavfile.read("../data/Xe.wav")

num_window_size = 2000

w = []

N = 5000
K = 3000
data2 = data[5000:5000+int(N)]
d = []
for k in range(K):
    dk = 0
    for m in range(N):
        dk += abs(data2[m] - data2[m-k])
    d.append(dk)

def calc_T(a):
    arr_i = []
    for i in range(1,len(a)):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            arr_i.append(i)
    return arr_i

plt.plot(d)
plt.show()