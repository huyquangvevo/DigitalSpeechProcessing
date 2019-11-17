from scipy.io.wavfile import read
import matplotlib.pyplot as plt 
import numpy as np
import math

# data = read("./data/Xe.wav")
fs, signal = read("../data/Xe.wav")

print(fs)
print(len(signal))