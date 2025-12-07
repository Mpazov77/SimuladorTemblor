# SimuladorTemblor

Simulador de terremoto para edificios de 11 niveles. Este proyecto permite simular el efecto de terremotos en un edificio de 11 pisos y visualizar los daños causados.

## Características

- **Edificio de 11 niveles**: Estructura completa con 11 pisos (niveles 0-10)
- **Simulación de terremoto**: Simula el impacto de terremotos con diferentes intensidades (escala Richter 0.0-10.0)
- **Análisis de daños**: Calcula el desplazamiento y daño en cada nivel
- **Visualización**: Muestra el estado del edificio antes y después del terremoto

## Estructura del Edificio

El edificio tiene las siguientes características:
- **Número de niveles**: 11 (del 0 al 10)
- **Altura por nivel**: 3.0 metros
- **Altura total**: 33.0 metros

Cada nivel puede experimentar:
- Desplazamiento horizontal durante un terremoto
- Daño estructural (medido en porcentaje)

## Uso

### Ejecutar el simulador interactivo

```bash
python3 simulador.py
```

El simulador ofrece las siguientes opciones:
1. Simular terremoto con intensidad personalizada
2. Ver el estado actual del edificio
3. Reiniciar el edificio a su estado original
4. Salir del programa

### Uso programático

```python
from edificio import Edificio

# Crear un edificio de 11 niveles
edificio = Edificio("Mi Edificio")

# Mostrar estructura inicial
edificio.mostrar_estructura()

# Simular un terremoto de intensidad 6.5
edificio.aplicar_terremoto(6.5)

# Mostrar estado después del terremoto
edificio.mostrar_estructura()

# Ver estado general
print(f"Estado del edificio: {edificio.get_estado()}")
```

## Ejecutar Tests

```bash
python3 test_edificio.py
```

## Archivos

- `edificio.py`: Clase principal del edificio y sus niveles
- `simulador.py`: Programa interactivo para ejecutar simulaciones
- `test_edificio.py`: Tests unitarios para validar la funcionalidad

## Estados del Edificio

El edificio puede estar en los siguientes estados después de un terremoto:
- **Intacto**: Sin daños
- **Daño Leve**: Daños menores, edificio estable
- **Daño Moderado**: Daños considerables, requiere inspección
- **Daño Severo**: Daños graves, puede ser peligroso
- **Colapso Inminente**: Daños críticos, evacuación necesaria