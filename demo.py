#!/usr/bin/env python3
"""
Demo script to showcase the 11-level building and earthquake simulation
"""

from edificio import Edificio
import time


def main():
    print("\n" + "="*60)
    print("DEMOSTRACIÓN - EDIFICIO DE 11 NIVELES".center(60))
    print("="*60)
    
    # Create the 11-level building
    edificio = Edificio("Edificio de 11 Niveles")
    
    print("\n1. Creando edificio de 11 niveles...")
    print("-" * 60)
    edificio.mostrar_estructura()
    
    input("\nPresione Enter para continuar...")
    
    # Simulate a light earthquake
    print("\n2. Simulando terremoto leve (intensidad 3.5)...")
    print("-" * 60)
    edificio.aplicar_terremoto(3.5)
    edificio.mostrar_estructura()
    
    input("\nPresione Enter para continuar...")
    
    # Simulate a moderate earthquake
    print("\n3. Simulando terremoto moderado (intensidad 6.0)...")
    print("-" * 60)
    edificio.aplicar_terremoto(6.0)
    edificio.mostrar_estructura()
    
    input("\nPresione Enter para continuar...")
    
    # Simulate a strong earthquake
    print("\n4. Simulando terremoto fuerte (intensidad 8.5)...")
    print("-" * 60)
    edificio.aplicar_terremoto(8.5)
    edificio.mostrar_estructura()
    
    print("\n" + "="*60)
    print("FIN DE LA DEMOSTRACIÓN".center(60))
    print("="*60)
    print("\nResumen:")
    print(f"- Edificio: {edificio.nombre}")
    print(f"- Número de niveles: {edificio.num_niveles}")
    print(f"- Altura total: {edificio.get_altura_total():.1f} metros")
    print(f"- Estado final: {edificio.get_estado()}")
    print("\nUse 'python3 simulador.py' para una experiencia interactiva.")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrumpida.")
    except EOFError:
        print("\n\nDemo finalizada.")
