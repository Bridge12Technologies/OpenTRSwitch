import skrf
import matplotlib.pyplot as plt
import numpy as np
import pathlib
base=pathlib.Path(__file__).parent.parent

dataset_s21 = base.joinpath("Data/S21_meas1.s2p") # TX -> RX
dataset_s23 = base.joinpath("Data/S23_meas2.s2p") # Probe -> RX

s21_skrf=skrf.Touchstone(str(dataset_s21))
data=s21_skrf.get_sparameter_data(format='db')
print(data)
freq=np.array((data["frequency"]).astype(float))/1e6
s21 = data["S21DB"]
s11 = data["S11DB"]


s23_skrf=skrf.Touchstone(str(dataset_s23))
data=s23_skrf.get_sparameter_data(format='db')
s23 = data["S21DB"]

plt.plot(freq,s21,label='S21: TX -> RX')
plt.plot(freq,s11,label='S11: TX')
plt.plot(freq,s23,label='S23: Probe -> RX')
plt.legend(fontsize=16,loc=7)
plt.title('TX/RX Characterization',fontsize=18)
plt.xlim((10,20))
plt.ylim((-45,1))
plt.xlabel('Frequency (MHz)',fontsize=18)
plt.ylabel('S-prm (dB) ',fontsize=18)
plt.tick_params(axis='both',labelsize=12)
plt.show()
#dataDNP=dnp.load([str(dataset_s21),str(dataset_s23)],coord=[0,1])


