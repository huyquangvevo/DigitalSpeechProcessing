# from scipy.io.wavfile import read
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.fft import fft, fftshift
#
# data = read("Xe.wav")
# # print(data[1])
# audio = data[1]
# # print()
#
# au = []
# k = 1000
#
# a = []
# for i in range(len(audio)):
#     if abs(audio[i]) < 11000:
#         a.append(float(0))
#         # print(a[0])
#         # break
#     else:
#         # print(i)
#         a.append(float(audio[i]))
# print(len(audio))
# print(len(a))
# # audio = a
#
# for idx in range(k):
#     r = 0
#     for i in range(1999-k):
#         # l = 1
#         # if abs(audio[5000+i]) < 11000 or abs(audio[5000+i+idx]) < 11000:
#             # l = 0
#         r += a[5000+i]*a[5000+i+idx]
#     au.append(r)
#
# # au.sort()
#
#
# plt.plot(au)
# plt.show()




import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wf

(fs, data) = wf.read('./data/Xe.wav')
print(np.max(data))
# # N = 300
# K = 150
# data1 = np.zeros(150)
for i in range(0, int(len(data) / 300)):
    dataTemp = data[i:300]
data1 = np.zeros(len(data))
for i in range(0, len(data)-1):
    if data[i] > 11000:
        print(i)
        data1[i] = data[i]-11000
    elif data[i] < -11000:
        print(i)
        data1[i] = data[i]+11000
data2 = np.zeros(1000)
for a in range(0,1000):
    # temp = 0
    for j in range(0,1999-a):
        data2[a] = data2[a]+data1[5000+j]*data1[5000+j+a]
    kk =1
data3 = np.zeros(1000)
for a in range(0,1000):
    # temp = 0
    for j in range(0,1999-a):
        data3[a] = data3[a]+np.abs(data1[7000+j] - data1[7000+j+a])



# plt.specgram(data, Fs = ra)
# plt.show()

# mau = 512
# a = 0.96
# data1 = np.zeros(mau)
# data2 = np.zeros(mau)

# for i in range(0,mau):
#     if i%512 == 0:
#         data1[i] = data[i]
#     else:
#         data1[i] = data[i-1]-a*data1[i-1]
# data4 = data1
# plt.plot(data4)
#
#
# cuaso = np.hamming(mau)
# for i in range(0,512):
#     data2[i] = data1[i]*cuaso[i%512]
# data2 = np.abs(np.fft.fft(data2))
# maxa = np.max(data2)
# # data2 = -20* np.log10(data2/maxa)
# data2 = np.fft.ifft(data2)
# data3 = data2[0:256]

# # c = 1
# # data1 = np.zeros(len(data))
# # for i in range(0, int(2*(len(data)-1)/mau), 1):
# #     for j in range(int(i*mau), int((i+2)*mau)):
# #     data1[i] = data1[i]
#     # bbb = cuaso[int(i%mau)]
#     # data1[i] = int(bbb*data[i])
#
# # data2 = np.zeros(int((len(data1)-1)/(mau*0.5)))
# # data3 = np.zeros(int((len(data1)-1)/mau))
# # for i in range(0, int((len(data1)-1)/(mau))*2):
# #     for j in range(int(((i-1)/2)*(len(data1)-1)/mau),int(((i+1)/2)*(len(data1)-1)/mau) ):
# #         data2[i] = data2[i]+data1[j]*data1[j]
#
#         # data3[i] = data2[i]+data1[j]*data1[j]
#
# # xử lý đòng hình suy ra s mũ
# #  Biến đổi fourier tính bổ biên độ
# # vẽ history diagram
#
#
#
#
#
plt.plot(data3)
# plt.plot(data2)
# plt.plot(data)
# plt.xlabel("ms")
# plt.ylabel("aaa")
plt.show()
