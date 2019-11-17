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

# for i in range(0,len(data)-int(num_window_size),int(num_window_size/2)):
# for i in range(5000,5001,int(num_window_size/2)):

data1 = np.zeros(len(data))
## Han che
for i in range(len(data1)):
    if abs(data[i])>16000:
        data1[i] = data[i]
## tinh r
N = 2000
K = 1000
r = []
r_list = []
# for i in range(5000,len(data1)-int(num_window_size),int(num_window_size/2)):
for i in range(1000,len(data1)-int(num_window_size),int(num_window_size/2)):
    print(i)
    data2 = data1[i:i+int(N)]
    for k in range(K):
        rk = 0
        for j in range(len(data2)-1-k):
            rk += data2[j]*data2[j+k]
            # print(data[j])
        r.append(rk)
    r_list.append(r)
def calc_T(a):
    arr_i = []
    for i in range(1,len(a)):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            arr_i.append(i)
    return arr_i
# print(calc_T(r))
# print((1.0/f)*20*(calc_T(r)[0]))
t = []
for r in r_list:
    t.append(calc_T(r)[0])
print(t)
plt.plot(t)
plt.show()

# print(data)