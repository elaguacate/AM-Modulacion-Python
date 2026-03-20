import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy import signal

# Configuración general
fs = 10000  # Frecuencia de muestreo (Hz)
T = 1.0     # Duración total (s)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# 1. Señal de mensaje m(t): suma de tonos (baja frecuencia)
fm1, fm2 = 50, 120  # Hz
Am1, Am2 = 1, 0.5
m = Am1 * np.cos(2 * np.pi * fm1 * t) + Am2 * np.cos(2 * np.pi * fm2 * t)

# 2. Señal portadora c(t)
fc = 2000  # Hz (alta frecuencia)
Ac = 2.0
c = Ac * np.cos(2 * np.pi * fc * t)

# 3. Modulación AM: s(t) = [Ac + ka * m(t)] * c(t), ka=índice de modulación
ka = 0.8  # Índice <1 para evitar sobremodulación
s = (Ac + ka * m) * c

# 4. Análisis en dominio del tiempo
plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(t[:500], m[:500])  # Primeros 0.05s
plt.title('Señal de Mensaje m(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t[:500], s[:500])
plt.title('Señal Modulada AM s(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t[:500], c[:500])
plt.title('Señal Portadora c(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Análisis en frecuencia (FFT)
N = len(t)
freq = fftfreq(N, 1/fs)

S_m = np.abs(fft(m)) / N
S_s = np.abs(fft(s)) / N

plt.figure(figsize=(12, 4))
plt.subplot(1,2,1)
plt.plot(freq[:N//2], 2 * S_m[:N//2])
plt.title('Espectro Mensaje m(t)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, 500)
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(freq[:N//2], 2 * S_s[:N//2])
plt.title('Espectro Señal Modulada s(t)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, 2500)
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Introducir ruido (AWGN)
SNR_dB = 20  # Relación señal-ruido (dB)
signal_power = np.mean(s**2)
noise_power = signal_power / (10**(SNR_dB/10))
noise = np.random.normal(0, np.sqrt(noise_power), len(s))
s_noisy = s + noise

# 7. Atenuación (factor 0.5)
s_attenuated = 0.5 * s

# 8. Distorsión (armónicos en mensaje)
m_distorted = m + 0.2 * m**3  # Distorsión no lineal cúbica
s_distorted = (Ac + ka * m_distorted) * c

# 9. Gráficos comparativos con ruido
plt.figure(figsize=(12, 10))

plt.subplot(4,1,1)
plt.plot(t[:200], s[:200], label='Original')
plt.plot(t[:200], s_noisy[:200], label='Con Ruido (SNR=20dB)')
plt.title('Efecto del Ruido')
plt.legend()
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(t[:200], s[:200], label='Original')
plt.plot(t[:200], s_attenuated[:200], label='Atenuada (x0.5)')
plt.title('Efecto de Atenuación')
plt.legend()
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t[:200], s[:200], label='Original')
plt.plot(t[:200], s_distorted[:200], label='Distorsionada')
plt.title('Efecto de Distorsión')
plt.legend()
plt.grid(True)

# Espectro con ruido
S_noisy = np.abs(fft(s_noisy)) / N
plt.subplot(4,1,4)
plt.plot(freq[:N//2], 2 * S_s[:N//2], label='Original')
plt.plot(freq[:N//2], 2 * S_noisy[:N//2], label='Con Ruido')
plt.title('Espectro con Ruido')
plt.xlabel('Frecuencia (Hz)')
plt.legend()
plt.xlim(0, 2500)
plt.grid(True)

plt.tight_layout()
plt.show()

# 10. Demodulación simple (envolvente)
from scipy.signal import hilbert
analytic_signal = hilbert(s)
envelope = np.abs(analytic_signal)
recovered_m = envelope - Ac  # Aproximación

plt.figure(figsize=(10, 4))
plt.plot(t[:500], m[:500], label='Original m(t)')
plt.plot(t[:500], recovered_m[:500]/ka, label='Recuperada')
plt.title('Demodulación (Envolvente)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()

print("Análisis completado. Observaciones:")
print("- Banda lateral: fc ± fm visible en espectro.")
print("- Ruido degrada SNR, afecta demodulación.")
print("- Atenuación reduce amplitud uniformemente.")
print("- Distorsión introduce armónicos en bajas frecuencias.")[web:4][web:2]
