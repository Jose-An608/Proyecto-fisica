import math

class CalculadoraMAS:
    def __init__(self, amplitud=None, frecuencia=None, periodo=None):
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.periodo = periodo
        self.omega = None  # Frecuencia angular

    def calcular_parametros(self):
        """Calcula parámetros del MAS"""
        # Si tenemos periodo
        if self.periodo is not None:
            self.omega = 2 * math.pi / self.periodo
            self.frecuencia = 1 / self.periodo
        
        # Si tenemos frecuencia
        elif self.frecuencia is not None:
            self.periodo = 1 / self.frecuencia
            self.omega = 2 * math.pi * self.frecuencia
        
        # Cálculos con amplitud
        if self.amplitud is not None and self.omega is not None:
            velocidad_max = self.amplitud * self.omega
            aceleracion_max = self.amplitud * (self.omega**2)
            
            return {
                'Amplitud': self.amplitud,
                'Periodo': self.periodo,
                'Frecuencia': self.frecuencia,
                'Frecuencia Angular (ω)': self.omega,
                'Velocidad Máxima': velocidad_max,
                'Aceleración Máxima': aceleracion_max
            }
        
        return {}

    def calcular_variables(self, tiempo=0):
        """Calcula variables en un tiempo específico"""
        if self.amplitud is None or self.omega is None:
            return None
        
        desplazamiento = self.amplitud * math.sin(self.omega * tiempo)
        velocidad = -self.amplitud * self.omega * math.cos(self.omega * tiempo)
        aceleracion = -self.amplitud * (self.omega**2) * math.sin(self.omega * tiempo)
        
        return {
            'Desplazamiento': desplazamiento,
            'Velocidad': velocidad,
            'Aceleración': aceleracion
        }