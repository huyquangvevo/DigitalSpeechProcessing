from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

rate, data = read('Xe.wav')


def config_filter(data):
    out = []
    for i in range(1, len(data), 1):
        out.append(data[i] - 0.98 * data[i - 1])
    return out


# fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = pl.subplots(7, 1, sharex=False)

sizecut = 512
start = int(0.4 * rate)

sg = data[start:start + sizecut]
pl.plot(sg)
pl.show()
