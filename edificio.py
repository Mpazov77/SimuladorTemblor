"""
Edificio - Building class for earthquake simulator
Represents an 11-level building structure
"""


class Nivel:
    """Represents a single level/floor of the building"""
    
    def __init__(self, numero, altura=3.0):
        """
        Initialize a building level
        
        Args:
            numero (int): Level number (0 is ground floor)
            altura (float): Height of the level in meters (default 3.0m)
        """
        self.numero = numero
        self.altura = altura
        self.desplazamiento = 0.0  # Horizontal displacement due to earthquake
        self.danio = 0  # Damage level (0-100%)
        
    def __str__(self):
        return f"Nivel {self.numero}: Altura={self.altura}m, Desplazamiento={self.desplazamiento:.2f}m, Daño={self.danio}%"


class Edificio:
    """Represents an 11-level building for earthquake simulation"""
    
    def __init__(self, nombre="Edificio de 11 Niveles"):
        """
        Initialize an 11-level building
        
        Args:
            nombre (str): Name of the building
        """
        self.nombre = nombre
        self.num_niveles = 11
        self.niveles = []
        
        # Create 11 levels (0-10)
        for i in range(self.num_niveles):
            self.niveles.append(Nivel(i, altura=3.0))
    
    def get_altura_total(self):
        """Get total height of the building"""
        return sum(nivel.altura for nivel in self.niveles)
    
    def aplicar_terremoto(self, intensidad):
        """
        Simulate earthquake effects on the building
        
        Args:
            intensidad (float): Earthquake intensity (0.0 to 10.0 Richter scale)
        """
        import math
        
        # Higher levels experience more displacement
        for i, nivel in enumerate(self.niveles):
            # Displacement increases with height and intensity
            factor_altura = (i + 1) / self.num_niveles
            nivel.desplazamiento = intensidad * 0.1 * factor_altura * (1 + math.sin(i))
            
            # Damage calculation based on displacement
            if nivel.desplazamiento > 0.5:
                nivel.danio = min(100, int((nivel.desplazamiento - 0.5) * 50))
    
    def get_estado(self):
        """Get current state of the building"""
        danio_total = sum(nivel.danio for nivel in self.niveles) / self.num_niveles
        
        if danio_total == 0:
            return "Intacto"
        elif danio_total < 20:
            return "Daño Leve"
        elif danio_total < 50:
            return "Daño Moderado"
        elif danio_total < 80:
            return "Daño Severo"
        else:
            return "Colapso Inminente"
    
    def mostrar_estructura(self):
        """Display the building structure"""
        print(f"\n{'='*60}")
        print(f"{self.nombre:^60}")
        print(f"{'='*60}")
        print(f"Número de Niveles: {self.num_niveles}")
        print(f"Altura Total: {self.get_altura_total():.1f} metros")
        print(f"Estado: {self.get_estado()}")
        print(f"{'='*60}\n")
        
        # Display levels from top to bottom
        for nivel in reversed(self.niveles):
            barra = "█" * max(1, 20 - int(nivel.desplazamiento * 10))
            print(f"{nivel}")
    
    def __str__(self):
        return f"{self.nombre} - {self.num_niveles} niveles, Altura total: {self.get_altura_total():.1f}m"
