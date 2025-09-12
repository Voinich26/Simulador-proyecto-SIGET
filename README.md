
# Simulador de Planificación de Proyectos SIGET

## Descripción
Simulador de planificación de procesos para el Sistema Inteligente de Gestión del Tráfico (SIGET). Este simulador implementa diferentes algoritmos de planificación de procesos y visualiza los estados por los que pasan los procesos durante su ejecución.

## Características

### Procesos del SIGET
El simulador incluye tres tipos de procesos del sistema de tráfico:

1. **Monitoreo de Tráfico**: Procesos que supervisan el flujo vehicular
2. **Gestión de Semáforos**: Procesos que controlan la sincronización de semáforos
3. **Análisis de Datos**: Procesos que procesan información estadística del tráfico

### Atributos de Procesos
- **Tiempo de Irrupción**: Momento en que el proceso llega al sistema
- **Prioridad de Alerta**: Nivel de urgencia (1-5, donde 1 es máxima prioridad)
- **Tamaño de Datos**: Cantidad de información en MB que maneja el proceso
- **Tiempo de Ejecución**: Duración necesaria para completar el proceso

### Algoritmos de Planificación
1. **FIFO (First In, First Out)**: Procesos se ejecutan en orden de llegada
2. **SJF (Shortest Job First)**: Procesos más cortos se ejecutan primero
3. **Prioridad**: Procesos con mayor prioridad (menor número) se ejecutan primero
4. **Round Robin**: Procesos se ejecutan en turnos con quantum configurable

### Estados de Procesos
- **Nuevo**: Proceso recién creado
- **Listo**: Proceso esperando ser ejecutado
- **En Ejecución**: Proceso actualmente ejecutándose
- **Bloqueado**: Proceso esperando por un recurso
- **Terminado**: Proceso completado

## Instalación y Ejecución

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas adicionales

### Ejecución
```bash
python simulador_siget.py
```

## Uso del Simulador

1. **Seleccionar Algoritmo**: Usar el menú desplegable para elegir el algoritmo de planificación
2. **Configurar Quantum**: Para Round Robin, ajustar el valor del quantum (1-10)
3. **Crear Procesos**: Usar el botón "Crear Procesos Ejemplo" para generar procesos de prueba
4. **Ejecutar Simulación**: Presionar "Ejecutar Simulación" para iniciar la simulación
5. **Observar Resultados**: La interfaz muestra en tiempo real:
   - Estado actual de cada proceso
   - Tiempo de simulación
   - Proceso en ejecución
   - Estadísticas de rendimiento
   - Log de eventos

## Interfaz Gráfica

### Panel Principal
- **Tabla de Procesos**: Muestra todos los procesos con sus atributos y estados actuales
- **Información de Simulación**: Tiempo actual, proceso en ejecución y estadísticas
- **Log de Eventos**: Registro detallado de todos los eventos durante la simulación

### Controles
- **Algoritmo de Planificación**: Selección del algoritmo a utilizar
- **Quantum**: Configuración del tiempo de quantum para Round Robin
- **Botones de Control**: Ejecutar, Resetear y Crear Procesos

## Características Técnicas

### Arquitectura
- **Programación Orientada a Objetos**: Uso de clases para procesos y simulador
- **Hilos de Ejecución**: Simulación ejecutándose en hilo separado para no bloquear la interfaz
- **Actualización en Tiempo Real**: Interfaz se actualiza durante la ejecución

### Algoritmos Implementados
- **FIFO**: Ordenamiento por tiempo de irrupción
- **SJF**: Ordenamiento por tiempo de ejecución
- **Prioridad**: Ordenamiento por prioridad de alerta
- **Round Robin**: Ejecución por turnos con quantum configurable

## Archivos del Proyecto

- `simulador_siget.py`: Código principal del simulador
- `requirements.txt`: Requisitos del sistema
- `README.md`: Documentación del proyecto
- `relatoria_tecnica.txt`: Documento técnico detallado

## Autor
Simulador desarrollado para el curso de Sistemas Operativos - SIGET


