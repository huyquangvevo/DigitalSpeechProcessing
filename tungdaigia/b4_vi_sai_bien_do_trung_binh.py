from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# f,data = wavfile.read("Xe.wav")
f,data = wavfile.read("Xe.wav")
print(f)
print(len(data))
num_window_size = 2000
# time = [(1.0/f)*i*20 for i in range(len(data))]
print(num_window_size)
w = []
## tinh r
N = 2000
K = 1000
data2 = data[5000:5000+int(N)]
## tinh D
d = []
for k in range(K):
    dk = 0
    for m in range(N):
        dk += abs(data2[m]-data2[m-k])
        # print(data[j])
    d.append(dk)

def calc_T(a):
    arr_i = []
    for i in range(1,len(a)):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            arr_i.append(i)
    return arr_i
# print(calc_T(r))
plt.plot(d)
plt.show()

# print(data)