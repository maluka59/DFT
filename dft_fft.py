import numpy as np
import time 
from prettytable import PrettyTable


# Hier wird ein Testsignal erzeugt mit variabeler Länge 
def f(x):
    y = 0
    result = []
    for _ in x:
        result.append(y)
        y += np.random.normal(scale=1)
    return np.array(result)


# Diese Methode: implementiert Diskrete Fourier Transformation als Matrixmultiplikation nach der Formel 
def diy_fft(x):
	N=len(x)
	X = np.zeros(N, dtype=np.complex64)
	for k in range(N):
		for n in range(N):
			X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

#Tabelle zum Vergleichen erstellen
myTable = PrettyTable(["Signale", "Zeit unserer Methode", "Zeit der Methode von numpy.fft()"])

#Laufzeit vom ersten Testsignal mit der Länge 1000 ermitteln(mit von uns selbstgeschriebener Methode)
start = time.time()
signal_1 = np.arange(1000)
diy_fft(f(signal_1))
end = time.time()
si_diy1=end - start
#Laufzeit vom ersten Testsignal mit der Länge 1000 ermitteln(von mumpy,fft())
start = time.time()
X_1000 = np.fft.fft(signal_1)
end = time.time()
si_fft1=end - start

#Erste Zeile der Tabelle mit den Ergebnissen der Laufzeit auffüllen
myTable.add_row(["Testsignal mit der Länge 1000", si_diy1, si_fft1])
print(myTable)

#Laufzeit vom ersten Testsignal mit der Länge 4096 ermitteln(mit von uns selbstgeschriebener Methode)
start = time.time()
signal_2 = np.arange(4096)
diy_fft(f(signal_2))
end = time.time()
si_diy2=end - start

#Laufzeit vom ersten Testsignal mit der Länge 4096 ermitteln(von mumpy,fft())
start = time.time()
X_4096 = np.fft.fft(signal_2)
end = time.time()
si_fft2=end - start

#Zweite Zeile der Tabelle mit den Ergebnissen der Laufzeit auffüllen
myTable.add_row(["Testsignal mit der Länge 4096", si_diy2, si_fft2])
print(myTable)

#Laufzeit vom ersten Testsignal mit der Länge 10000 ermitteln(mit von uns selbstgeschriebener Methode)
start = time.time()
signal_3 = np.arange(10000)
diy_fft(f(signal_3))
end = time.time()
si_diy3=end - start

#Laufzeit vom ersten Testsignal mit der Länge 10000 ermitteln(von mumpy,fft())
start = time.time()
X_10000 = np.fft.fft(signal_3)
end = time.time()
si_fft3=end - start

#Dritte Zeile der Tabelle mit den Ergebnissen der Laufzeit auffüllen
myTable.add_row(["Testsignal mit der Länge 10000", si_diy3, si_fft3])
print(myTable)
