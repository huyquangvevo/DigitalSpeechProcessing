from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np

# data = read("./data/Xe.wav")
data = read("./data/khoosoothunhus.wav")
def emergy(data):
    return (data*2).sum()

def emergy2(data):
    return data*data
# print(data[0])
# print(data[1][:-2000])
# exit()
# print(data[1])
audio = data[1]
h = audio*np.hamming(len(audio))
h = np.apply_along_axis(emergy2,0,h)
print(h.shape)
plt.plot(np.arange(len(h))/data[0], h)
plt.show()
exit()



print(np.arange(len(audio))/data[0])

# plt.plot(audio[0:1024])
plt.plot(np.arange(len(audio))/data[0], audio)
plt.ylabel("Ampitude")
plt.xlabel("Time(ms)")

plt.title("Sample wav")
plt.show()


