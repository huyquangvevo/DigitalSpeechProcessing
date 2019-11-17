import matplotlib.pyplot as plt
import numpy as np
import wave 
import sys
# import scipy.io.wavfile import read

spf = wave.open('./data/khoosoothunhus.wav','r')

singal = spf.readframes(-1) 
singal = np.fromstring(singal,'Int16') 
# print(singal)

plt.figure(1)
plt.title('Signal wave...')
plt.plot(singal)
plt.show()