# Modulación en Amplitud (AM) con Python

## Descripción
Implementación de un sistema de modulación en amplitud (AM) usando Python.
Se analiza el comportamiento de la señal en los dominios del tiempo y frecuencia,
evaluando el impacto de ruido, distorsión y atenuación en la señal modulada.

## Conceptos aplicados
- Modulación en amplitud: `s(t) = [Ac + ka·m(t)] · cos(2πfct)`
- Análisis en dominio del tiempo y frecuencia (FFT)
- Ruido AWGN, distorsión no lineal y atenuación
- Demodulación por envolvente (Transformada de Hilbert)

## Requisitos
```bash
pip install numpy scipy matplotlib
