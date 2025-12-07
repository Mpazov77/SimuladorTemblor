#!/usr/bin/env python3
"""
Simulador de Temblor - Earthquake Simulator
Main program to simulate earthquakes on an 11-level building
"""

from edificio import Edificio
import sys


def main():
    """Main function to run the earthquake simulator"""
    
    print("\n" + "="*60)
    print("SIMULADOR DE TERREMOTO".center(60))
    print("="*60)
    
    # Create 11-level building
    edificio = Edificio("Edificio de 11 Niveles")
    
    print("\nCreando edificio de 11 niveles...")
    edificio.mostrar_estructura()
    
    # Interactive simulation
    while True:
        print("\n" + "-"*60)
        print("Opciones:")
        print("1. Simular terremoto")
        print("2. Ver estado del edificio")
        print("3. Reiniciar edificio")
        print("4. Salir")
        print("-"*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                try:
                    intensidad = float(input("Ingrese la intensidad del terremoto (0.0-10.0 escala Richter): "))
                    if 0.0 <= intensidad <= 10.0:
                        print(f"\nSimulando terremoto de intensidad {intensidad}...")
                        edificio.aplicar_terremoto(intensidad)
                        edificio.mostrar_estructura()
                    else:
                        print("Error: La intensidad debe estar entre 0.0 y 10.0")
                except ValueError:
                    print("Error: Ingrese un número válido")
            
            elif opcion == "2":
                edificio.mostrar_estructura()
            
            elif opcion == "3":
                edificio = Edificio("Edificio de 11 Niveles")
                print("\nEdificio reiniciado.")
                edificio.mostrar_estructura()
            
            elif opcion == "4":
                print("\n¡Gracias por usar el Simulador de Terremoto!")
                break
            
            else:
                print("Opción no válida. Por favor seleccione 1-4.")
        
        except KeyboardInterrupt:
            print("\n\n¡Simulación interrumpida!")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
