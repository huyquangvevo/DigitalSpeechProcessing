from scipy.io import wavfile
import matplotlib.pyplot as plt 
import numpy as np 

f,data = wavfile.read('../data/Xe.wav')
print(f)
print(len(data))