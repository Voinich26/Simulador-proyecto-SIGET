# Instrucciones de Uso - Simulador SIGET

## 🚀 Inicio Rápido

### Opción 1: Ejecución Directa
```bash
python simulador_siget.py
```

### Opción 2: Ejecución con Verificaciones
```bash
python ejecutar_simulador.py
```

## 📋 Pasos para Usar el Simulador

### 1. Preparación
- Asegúrate de tener Python 3.7 o superior instalado
- Verifica que tkinter esté disponible (generalmente incluido con Python)

### 2. Crear Procesos
1. Haz clic en **"Crear Procesos Ejemplo"** para generar procesos de prueba del SIGET
2. Los procesos incluyen:
   - Monitoreo de Tráfico (alta prioridad)
   - Gestión de Semáforos (prioridad media)
   - Análisis de Datos (prioridad variable)

### 3. Configurar Algoritmo
1. Selecciona el algoritmo de planificación del menú desplegable:
   - **FIFO**: First In, First Out
   - **SJF**: Shortest Job First
   - **Prioridad**: Por prioridad de alerta
   - **Round Robin**: Con quantum configurable

2. Para Round Robin, ajusta el quantum (1-10) según necesites

### 4. Ejecutar Simulación
1. Haz clic en **"Ejecutar Simulación"**
2. Observa cómo los procesos cambian de estado en tiempo real
3. Revisa las estadísticas de rendimiento

### 5. Interpretar Resultados

#### Tabla de Procesos
- **ID**: Identificador único del proceso
- **Nombre**: Nombre descriptivo del proceso
- **Tipo**: Categoría del proceso (Monitoreo, Semáforos, Análisis)
- **T. Irrupción**: Momento de llegada al sistema
- **T. Ejecución**: Tiempo total necesario para completar
- **Prioridad**: Nivel de urgencia (1-5, 1=máxima)
- **Tamaño (MB)**: Volumen de datos que maneja
- **Estado**: Estado actual del proceso
- **T. Restante**: Tiempo que falta para completar
- **T. Espera**: Tiempo que ha esperado en cola

#### Colores de Estado
- 🔵 **Azul claro**: Nuevo
- 🟡 **Amarillo**: Listo
- 🟢 **Verde**: En Ejecución
- 🔴 **Rojo**: Bloqueado
- 🔵 **Azul oscuro**: Terminado

#### Panel de Información
- **Tiempo Actual**: Tiempo transcurrido en la simulación
- **Proceso Actual**: Proceso que se está ejecutando
- **Estadísticas**: Métricas de rendimiento del algoritmo

## 🔧 Funcionalidades Avanzadas

### Comparar Algoritmos
1. Ejecuta la simulación con un algoritmo
2. Anota las estadísticas de rendimiento
3. Resetea la simulación
4. Cambia el algoritmo y ejecuta nuevamente
5. Compara los resultados

### Configurar Quantum (Round Robin)
- **Quantum pequeño (1-2)**: Mayor equidad, más cambios de contexto
- **Quantum grande (5-10)**: Menos cambios de contexto, posible inanición

### Analizar Diferentes Escenarios
- Crea procesos con diferentes prioridades
- Observa cómo cada algoritmo maneja la carga
- Compara tiempos de espera y respuesta

## 📊 Interpretación de Estadísticas

### Tiempo Promedio de Espera
- Indica cuánto tiempo esperan los procesos en cola
- Menor valor = mejor rendimiento

### Tiempo Promedio de Respuesta
- Tiempo total desde llegada hasta finalización
- Incluye tiempo de espera + tiempo de ejecución

### Tiempo Total de Simulación
- Duración total de la simulación
- Útil para comparar eficiencia de algoritmos

## 🐛 Solución de Problemas

### Error: "tkinter no está disponible"
**Solución**: Instalar tkinter según tu sistema operativo:
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- CentOS/RHEL: `sudo yum install tkinter`
- Windows: Generalmente incluido con Python

### Error: "Python 3.7+ requerido"
**Solución**: Actualizar Python a versión 3.7 o superior

### La simulación no inicia
**Solución**: 
1. Verifica que todos los archivos estén presentes
2. Usa `python ejecutar_simulador.py` para verificar el sistema

## 📚 Conceptos Educativos

### Estados de Procesos
- **Nuevo → Listo**: Proceso llega al sistema
- **Listo → En Ejecución**: Planificador selecciona el proceso
- **En Ejecución → Listo**: Quantum agotado (Round Robin)
- **En Ejecución → Terminado**: Proceso completado
- **En Ejecución → Bloqueado**: Esperando recurso (no implementado)

### Algoritmos de Planificación
- **FIFO**: Simple, justo, pero puede ser ineficiente
- **SJF**: Óptimo para tiempo de espera, requiere conocimiento previo
- **Prioridad**: Útil para sistemas críticos, puede causar inanición
- **Round Robin**: Equitativo, evita inanición, bueno para sistemas interactivos

## 🎯 Objetivos de Aprendizaje

Al usar este simulador, podrás:
1. Entender cómo funcionan los algoritmos de planificación
2. Visualizar los estados de los procesos
3. Comparar el rendimiento de diferentes algoritmos
4. Aplicar conceptos teóricos a un sistema real (SIGET)
5. Analizar métricas de rendimiento de sistemas operativos


