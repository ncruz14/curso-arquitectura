class Cita:
    def __init__(self, paciente, fecha, edad):
        self.name = paciente
        self.date = fecha
        self.old = edad

    def detalles(self):
        return f"Cita con {self.name} el {self.date}"
    
    def nombre_paciente(self):
        return self.name
    
    def edad_paciente(self):
        return f"La eddad del paciente es: {self.old}" 
