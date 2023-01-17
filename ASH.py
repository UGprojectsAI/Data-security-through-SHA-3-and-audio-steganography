from IPython.display import Audio
import librosa
import librosa.display
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sounddevice as sd
import soundfile as sf
import hashlib
import librosa

class ASH:
    d = 0
    samplerate = 0
    duration = 0
    password = ""
    yc, fsc = librosa.load("C://Users//shrey//dsaIIproject//ewe.wav")

    def record(self):
        self.d = int(input("Enter desired scaling value"))
        self.samplerate = int(input("Enter desired sampling rate : "))
        self.duration = int(input("Enter duration : "))
        f1 = open("C://Users//shrey//dsaIIproject//info.txt", "w")
        f1.write(str(self.d)+"\n")
        f1.write(str(self.samplerate)+"\n")
        print("start")
        mydata = sd.rec(int(self.samplerate * self.duration), samplerate=self.samplerate, channels=1, blocking=True)
        print("end")
        sd.wait()
        y1 = mydata.reshape(-1)
        y = y1 / self.d + self.yc[1:y1.shape[0] + 1]
        write('C://Users//shrey//dsaIIproject//fadeinto.wav', self.fsc, y)
        pd = input("Set a password : ")
        m = hashlib.sha3_512(pd.encode('UTF-8'))
        self.password = m.hexdigest()
        f1.write(self.password)

    def desteganography(self, audiofile):
        y1, fs1 = librosa.load(audiofile)
        d = int(input("Enter scaling value : "))
        f = int(input("Enter sampling rate : "))
        if d != self.d or f != self.samplerate:
            time = np.arange(0, 100000, 0.1)
            sin = np.tan(time)
            write('C://Users//shrey//dsaIIproject//fadeout.wav', 22050, sin)
        else:
            y = (y1 - self.yc[1:y1.shape[0] + 1]) * d
            write('C://Users//shrey//dsaIIproject//fadeout.wav', f, y)

    def Access(self):
        ep = input("Enter password : ")
        m1 = hashlib.sha3_512(ep.encode('UTF-8'))
        if (m1.hexdigest() == self.password):
            f = open("C://Users//shrey//dsaIIproject//my_file.txt", "w")
            x = "scaling value :" + str(self.d)
            y = "sampling rate : " + str(self.samplerate)
            f.write(x+"\n"+y)