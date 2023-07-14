import skrf
import matplotlib.pyplot as plt
import numpy as np
import pathlib
base=pathlib.Path(__file__).parent.parent

dataset_s21 = base.joinpath("Data/S21_meas1.s2p") # TX -> RX
dataset_s23 = base.joinpath("Data/S23_meas2.s2p") # Probe -> RX

s21_skrf=skrf.Touchstone(str(dataset_s21))
data=s21_skrf.get_sparameter_data(format='db')

freq=np.array((data["frequency"]).astype(float))/1e6

s21 = data["S21DB"]
s11 = data["S11DB"]
s23_skrf=skrf.Touchstone(str(dataset_s23))
data=s23_skrf.get_sparameter_data(format='db')
s23 = data["S21DB"]


# S21 - TX/RX isolation
plt.figure()
plt.plot(freq, s21, label = "S21 (TX/RX)")
plt.vlines(x = 15, ymin = -50, ymax = 0, linestyles = "dashed")
plt.xlim((10,25))
plt.ylim((-50,0))
plt.title("RX/TX Isolation")
plt.ylabel("S$_{21}$ (dB)")
plt.xlabel("Frequency (MHz)")
plt.grid(True)
plt.savefig("RX_TX_Isolation.png")
plt.show()


# S11 - TX Return Loss
plt.figure()
plt.plot(freq, s11, label = "S21 (TX/RX)")
plt.vlines(x = 15, ymin = -50, ymax = 0, linestyles = "dashed")
plt.xlim((10,25))
plt.ylim((-50,0))
plt.title("TX Return Loss")
plt.ylabel("S$_{11}$ (dB)")
plt.xlabel("Frequency (MHz)")
plt.grid(True)
plt.savefig("S11_TX_ReturnLoss.png")
plt.show()


# S21 - Probe -> RX
plt.figure()
plt.plot(freq, s23)
plt.vlines(x = 15, ymin = -1, ymax = 0, linestyles = "dashed")
plt.xlim((10,25))
plt.ylim((-1,0))
plt.title("Probe/RX Insertion Loss")
plt.ylabel("S$_{23}$ (dB)")
plt.xlabel("Frequency (MHz)")
plt.grid(True)
plt.savefig("S23_ProbeRXInsertionLoss.png")
plt.show()

