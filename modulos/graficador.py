import numpy as np
import matplotlib.pyplot as plt

class GraficadorMAS:
    @staticmethod
    def graficar_desplazamiento(amplitud, omega, tiempo_total=10):
        """Graficar desplazamiento"""
        t = np.linspace(0, tiempo_total, 200)
        x = amplitud * np.sin(omega * t)
        
        plt.figure(figsize=(10, 6))
        plt.plot(t, x)
        plt.title('Desplazamiento en MAS')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Desplazamiento (m)')
        plt.grid(True)
        plt.show()

    @staticmethod
    def graficar_velocidad(amplitud, omega, tiempo_total=10):
        """Graficar velocidad"""
        t = np.linspace(0, tiempo_total, 200)
        v = -amplitud * omega * np.cos(omega * t)
        
        plt.figure(figsize=(10, 6))
        plt.plot(t, v)
        plt.title('Velocidad en MAS')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Velocidad (m/s)')
        plt.grid(True)
        plt.show()

    @staticmethod
    def graficar_aceleracion(amplitud, omega, tiempo_total=10):
        """Graficar aceleración"""
        t = np.linspace(0, tiempo_total, 200)
        a = -amplitud * (omega**2) * np.sin(omega * t)
        
        plt.figure(figsize=(10, 6))
        plt.plot(t, a)
        plt.title('Aceleración en MAS')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Aceleración (m/s²)')
        plt.grid(True)
        plt.show()