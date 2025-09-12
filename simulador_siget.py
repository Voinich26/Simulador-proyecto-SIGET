import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
import random

class EstadoProceso(Enum):
    NUEVO = "Nuevo"
    LISTO = "Listo"
    EN_EJECUCION = "En Ejecución"
    BLOQUEADO = "Bloqueado"
    TERMINADO = "Terminado"

class TipoProceso(Enum):
    MONITOREO_TRAFICO = "Monitoreo de Tráfico"
    GESTION_SEMAFOROS = "Gestión de Semáforos"
    ANALISIS_DATOS = "Análisis de Datos"

@dataclass
class ProcesoSIGET:
    id: int
    nombre: str
    tipo: TipoProceso
    tiempo_irrupcion: int  # Tiempo de llegada
    tiempo_ejecucion: int  # Tiempo de CPU necesario
    prioridad_alerta: int  # 1-5 (1 = máxima prioridad)
    tamaño_datos: int  # MB
    estado: EstadoProceso = EstadoProceso.NUEVO
    tiempo_restante: int = 0
    tiempo_espera: int = 0
    tiempo_respuesta: int = 0
    tiempo_inicio: Optional[int] = None
    tiempo_fin: Optional[int] = None

class AlgoritmoPlanificacion:
    @staticmethod
    def fifo(procesos: List[ProcesoSIGET]) -> List[ProcesoSIGET]:
        """First In, First Out - Ordena por tiempo de irrupción"""
        return sorted(procesos, key=lambda p: p.tiempo_irrupcion)
    
    @staticmethod
    def sjf(procesos: List[ProcesoSIGET]) -> List[ProcesoSIGET]:
        """Shortest Job First - Ordena por tiempo de ejecución"""
        return sorted(procesos, key=lambda p: p.tiempo_ejecucion)
    
    @staticmethod
    def prioridad(procesos: List[ProcesoSIGET]) -> List[ProcesoSIGET]:
        """Por prioridad de alerta (menor número = mayor prioridad)"""
        return sorted(procesos, key=lambda p: p.prioridad_alerta)
    
    @staticmethod
    def round_robin(procesos: List[ProcesoSIGET], quantum: int = 2) -> List[ProcesoSIGET]:
        """Round Robin - Implementación especial con quantum"""
        # Para Round Robin, devolvemos la lista original ya que se maneja diferente
        return procesos

class SimuladorSIGET:
    def __init__(self):
        self.procesos: List[ProcesoSIGET] = []
        self.procesos_terminados: List[ProcesoSIGET] = []
        self.algoritmo_actual = "FIFO"
        self.quantum = 2
        self.tiempo_actual = 0
        self.ejecutando = False
        self.proceso_actual: Optional[ProcesoSIGET] = None
        self.cola_listos: List[ProcesoSIGET] = []
        
    def crear_procesos_ejemplo(self):
        """Crea procesos de ejemplo para el SIGET"""
        self.procesos = [
            ProcesoSIGET(1, "Monitoreo Centro", TipoProceso.MONITOREO_TRAFICO, 0, 8, 1, 150),
            ProcesoSIGET(2, "Semaforos Avenida Principal", TipoProceso.GESTION_SEMAFOROS, 2, 5, 2, 80),
            ProcesoSIGET(3, "Análisis Patrones", TipoProceso.ANALISIS_DATOS, 4, 12, 3, 300),
            ProcesoSIGET(4, "Monitoreo Periferia", TipoProceso.MONITOREO_TRAFICO, 6, 6, 2, 120),
            ProcesoSIGET(5, "Semaforos Intersección", TipoProceso.GESTION_SEMAFOROS, 8, 3, 1, 60),
            ProcesoSIGET(6, "Reporte Estadísticas", TipoProceso.ANALISIS_DATOS, 10, 7, 4, 200)
        ]
        
        # Inicializar tiempo restante
        for proceso in self.procesos:
            proceso.tiempo_restante = proceso.tiempo_ejecucion
    
    def resetear_simulacion(self):
        """Reinicia la simulación"""
        self.tiempo_actual = 0
        self.ejecutando = False
        self.proceso_actual = None
        self.cola_listos = []
        self.procesos_terminados = []
        
        for proceso in self.procesos:
            proceso.estado = EstadoProceso.NUEVO
            proceso.tiempo_restante = proceso.tiempo_ejecucion
            proceso.tiempo_espera = 0
            proceso.tiempo_respuesta = 0
            proceso.tiempo_inicio = None
            proceso.tiempo_fin = None
    
    def ejecutar_simulacion(self, callback_actualizacion=None):
        """Ejecuta la simulación con el algoritmo seleccionado"""
        self.resetear_simulacion()
        self.ejecutando = True
        
        # Crear cola de procesos ordenada según el algoritmo
        if self.algoritmo_actual == "FIFO":
            cola_procesos = AlgoritmoPlanificacion.fifo(self.procesos.copy())
        elif self.algoritmo_actual == "SJF":
            cola_procesos = AlgoritmoPlanificacion.sjf(self.procesos.copy())
        elif self.algoritmo_actual == "Prioridad":
            cola_procesos = AlgoritmoPlanificacion.prioridad(self.procesos.copy())
        else:  # Round Robin
            cola_procesos = self.procesos.copy()
        
        # Simular ejecución
        while cola_procesos or self.cola_listos or self.proceso_actual:
            # Actualizar estados de procesos que llegan
            for proceso in cola_procesos[:]:
                if proceso.tiempo_irrupcion <= self.tiempo_actual:
                    proceso.estado = EstadoProceso.LISTO
                    self.cola_listos.append(proceso)
                    cola_procesos.remove(proceso)
            
            # Seleccionar siguiente proceso
            if not self.proceso_actual and self.cola_listos:
                if self.algoritmo_actual == "Round Robin":
                    self.proceso_actual = self.cola_listos.pop(0)
                else:
                    # Para otros algoritmos, el orden ya está definido
                    self.proceso_actual = self.cola_listos.pop(0)
                
                self.proceso_actual.estado = EstadoProceso.EN_EJECUCION
                if self.proceso_actual.tiempo_inicio is None:
                    self.proceso_actual.tiempo_inicio = self.tiempo_actual
            
            # Ejecutar proceso actual
            if self.proceso_actual:
                tiempo_ejecucion = min(self.quantum if self.algoritmo_actual == "Round Robin" 
                                    else self.proceso_actual.tiempo_restante, 
                                    self.proceso_actual.tiempo_restante)
                
                # Simular ejecución
                time.sleep(0.5)  # Pausa visual
                
                self.proceso_actual.tiempo_restante -= tiempo_ejecucion
                self.tiempo_actual += tiempo_ejecucion
                
                # Actualizar tiempo de espera de otros procesos
                for proceso in self.cola_listos:
                    proceso.tiempo_espera += tiempo_ejecucion
                
                # Verificar si el proceso terminó
                if self.proceso_actual.tiempo_restante <= 0:
                    self.proceso_actual.estado = EstadoProceso.TERMINADO
                    self.proceso_actual.tiempo_fin = self.tiempo_actual
                    self.proceso_actual.tiempo_respuesta = (self.proceso_actual.tiempo_fin - 
                                                          self.proceso_actual.tiempo_irrupcion)
                    self.procesos_terminados.append(self.proceso_actual)
                    self.proceso_actual = None
                else:
                    # Para Round Robin, mover a la cola
                    if self.algoritmo_actual == "Round Robin":
                        self.proceso_actual.estado = EstadoProceso.LISTO
                        self.cola_listos.append(self.proceso_actual)
                        self.proceso_actual = None
            
            # Callback para actualizar la interfaz
            if callback_actualizacion:
                callback_actualizacion()
        
        self.ejecutando = False
        if callback_actualizacion:
            callback_actualizacion()

class InterfazSimulador:
    def __init__(self):
        self.simulador = SimuladorSIGET()
        self.ventana = tk.Tk()
        self.ventana.title("🚦 Simulador SIGET - Sistema Inteligente de Gestión del Tráfico")
        self.ventana.geometry("1400x900")
        self.ventana.configure(bg='#1a1a1a')
        
        # Configurar tema oscuro
        self.configurar_tema_oscuro()
        
        self.crear_interfaz()
        self.simulador.crear_procesos_ejemplo()
        self.actualizar_tabla()
    
    def configurar_tema_oscuro(self):
        """Configura el tema oscuro moderno"""
        # Colores del tema oscuro
        self.colores = {
            'fondo_principal': '#1a1a1a',
            'fondo_secundario': '#2d2d2d',
            'fondo_terciario': '#3d3d3d',
            'texto_principal': '#ffffff',
            'texto_secundario': '#b0b0b0',
            'texto_acento': '#00d4ff',
            'borde': '#4a4a4a',
            'boton_primario': '#00d4ff',
            'boton_secundario': '#6c757d',
            'boton_peligro': '#dc3545',
            'boton_exito': '#28a745',
            'boton_advertencia': '#ffc107',
            'tabla_fondo': '#2d2d2d',
            'tabla_seleccion': '#404040',
            'nuevo': '#17a2b8',
            'listo': '#ffc107',
            'ejecucion': '#28a745',
            'bloqueado': '#dc3545',
            'terminado': '#6c757d'
        }
        
        # Configurar estilo de ttk
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos personalizados
        style.configure('TLabel', background=self.colores['fondo_principal'], foreground=self.colores['texto_principal'])
        style.configure('TFrame', background=self.colores['fondo_principal'])
        style.configure('TLabelFrame', background=self.colores['fondo_principal'], foreground=self.colores['texto_principal'])
        style.configure('TLabelFrame.Label', background=self.colores['fondo_principal'], foreground=self.colores['texto_acento'])
        
        # Estilo para botones
        style.configure('Modern.TButton', 
                       background=self.colores['boton_primario'],
                       foreground='white',
                       font=('Segoe UI', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        style.map('Modern.TButton',
                 background=[('active', '#0099cc'),
                           ('pressed', '#0077aa')])
        
        # Estilo para combobox
        style.configure('Modern.TCombobox',
                       fieldbackground=self.colores['fondo_secundario'],
                       background=self.colores['fondo_secundario'],
                       foreground=self.colores['texto_principal'],
                       borderwidth=1,
                       relief='solid')
        
        # Estilo para treeview
        style.configure('Modern.Treeview',
                       background=self.colores['tabla_fondo'],
                       foreground=self.colores['texto_principal'],
                       fieldbackground=self.colores['tabla_fondo'],
                       borderwidth=1,
                       relief='solid')
        style.configure('Modern.Treeview.Heading',
                       background=self.colores['fondo_terciario'],
                       foreground=self.colores['texto_acento'],
                       font=('Segoe UI', 9, 'bold'),
                       relief='flat')
        style.map('Modern.Treeview',
                 background=[('selected', self.colores['tabla_seleccion'])])
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica del simulador con tema oscuro moderno"""
        # Título principal con gradiente visual
        frame_titulo = tk.Frame(self.ventana, bg=self.colores['fondo_secundario'], height=80)
        frame_titulo.pack(fill=tk.X, pady=(0, 10))
        frame_titulo.pack_propagate(False)
        
        titulo = tk.Label(frame_titulo, text="🚦 SIGET", 
                         font=("Segoe UI", 24, "bold"), 
                         bg=self.colores['fondo_secundario'], 
                         fg=self.colores['texto_acento'])
        titulo.pack(pady=15)
        
        subtitulo = tk.Label(frame_titulo, text="Sistema Inteligente de Gestión del Tráfico", 
                           font=("Segoe UI", 12), 
                           bg=self.colores['fondo_secundario'], 
                           fg=self.colores['texto_secundario'])
        subtitulo.pack()
        
        # Frame de controles con estilo moderno
        frame_controles = tk.Frame(self.ventana, bg=self.colores['fondo_secundario'], 
                                  relief=tk.RAISED, bd=1)
        frame_controles.pack(pady=10, padx=20, fill=tk.X)
        
        # Título de controles
        tk.Label(frame_controles, text="⚙️ Configuración de Simulación", 
                font=("Segoe UI", 14, "bold"), 
                bg=self.colores['fondo_secundario'], 
                fg=self.colores['texto_principal']).pack(pady=(15, 10))
        
        # Controles en una fila
        frame_controles_inner = tk.Frame(frame_controles, bg=self.colores['fondo_secundario'])
        frame_controles_inner.pack(pady=(0, 15))
        
        # Selección de algoritmo
        tk.Label(frame_controles_inner, text="Algoritmo:", 
                font=("Segoe UI", 11, "bold"), 
                bg=self.colores['fondo_secundario'], 
                fg=self.colores['texto_principal']).grid(row=0, column=0, padx=(20, 5), pady=5)
        
        self.var_algoritmo = tk.StringVar(value="FIFO")
        combo_algoritmo = ttk.Combobox(frame_controles_inner, textvariable=self.var_algoritmo,
                                      values=["FIFO", "SJF", "Prioridad", "Round Robin"],
                                      state="readonly", width=15, style='Modern.TCombobox')
        combo_algoritmo.grid(row=0, column=1, padx=5, pady=5)
        combo_algoritmo.bind("<<ComboboxSelected>>", self.cambiar_algoritmo)
        
        # Quantum para Round Robin
        tk.Label(frame_controles_inner, text="Quantum:", 
                font=("Segoe UI", 11, "bold"), 
                bg=self.colores['fondo_secundario'], 
                fg=self.colores['texto_principal']).grid(row=0, column=2, padx=(20, 5), pady=5)
        
        self.var_quantum = tk.StringVar(value="2")
        spin_quantum = tk.Spinbox(frame_controles_inner, from_=1, to=10, textvariable=self.var_quantum,
                                 width=5, bg=self.colores['fondo_terciario'], 
                                 fg=self.colores['texto_principal'],
                                 font=("Segoe UI", 10))
        spin_quantum.grid(row=0, column=3, padx=5, pady=5)
        
        # Botones de control con estilo moderno
        frame_botones = tk.Frame(self.ventana, bg=self.colores['fondo_principal'])
        frame_botones.pack(pady=15)
        
        btn_ejecutar = tk.Button(frame_botones, text="▶️ Ejecutar Simulación", 
                               command=self.ejecutar_simulacion, 
                               bg=self.colores['boton_exito'], fg='white',
                               font=("Segoe UI", 11, "bold"), 
                               padx=25, pady=8, relief=tk.FLAT,
                               cursor="hand2")
        btn_ejecutar.pack(side=tk.LEFT, padx=8)
        
        btn_resetear = tk.Button(frame_botones, text="🔄 Resetear", 
                               command=self.resetear_simulacion, 
                               bg=self.colores['boton_advertencia'], fg='white',
                               font=("Segoe UI", 11, "bold"), 
                               padx=25, pady=8, relief=tk.FLAT,
                               cursor="hand2")
        btn_resetear.pack(side=tk.LEFT, padx=8)
        
        btn_crear_procesos = tk.Button(frame_botones, text="➕ Crear Procesos", 
                                     command=self.crear_procesos_nuevos, 
                                     bg=self.colores['boton_primario'], fg='white',
                                     font=("Segoe UI", 11, "bold"), 
                                     padx=25, pady=8, relief=tk.FLAT,
                                     cursor="hand2")
        btn_crear_procesos.pack(side=tk.LEFT, padx=8)
        
        # Frame principal con dos columnas
        frame_principal = tk.Frame(self.ventana, bg=self.colores['fondo_principal'])
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Columna izquierda - Tabla de procesos
        frame_tabla = tk.LabelFrame(frame_principal, text="📊 Estado de Procesos", 
                                   font=("Segoe UI", 14, "bold"), 
                                   bg=self.colores['fondo_secundario'],
                                   fg=self.colores['texto_acento'],
                                   relief=tk.RAISED, bd=2)
        frame_tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Crear tabla de procesos con estilo moderno
        columnas = ("ID", "Nombre", "Tipo", "T. Irrupción", "T. Ejecución", 
                   "Prioridad", "Tamaño (MB)", "Estado", "T. Restante", "T. Espera")
        
        self.tabla_procesos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", 
                                          height=18, style='Modern.Treeview')
        
        for col in columnas:
            self.tabla_procesos.heading(col, text=col)
            self.tabla_procesos.column(col, width=90, anchor=tk.CENTER)
        
        scrollbar_tabla = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tabla_procesos.yview)
        self.tabla_procesos.configure(yscrollcommand=scrollbar_tabla.set)
        
        self.tabla_procesos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar_tabla.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        
        # Columna derecha - Información de simulación
        frame_info = tk.LabelFrame(frame_principal, text="📈 Información de Simulación", 
                                  font=("Segoe UI", 14, "bold"), 
                                  bg=self.colores['fondo_secundario'],
                                  fg=self.colores['texto_acento'],
                                  relief=tk.RAISED, bd=2)
        frame_info.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Información del algoritmo actual
        frame_algoritmo = tk.Frame(frame_info, bg=self.colores['fondo_secundario'])
        frame_algoritmo.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        self.label_algoritmo = tk.Label(frame_algoritmo, text="Algoritmo: FIFO", 
                                       font=("Segoe UI", 12, "bold"), 
                                       bg=self.colores['fondo_secundario'],
                                       fg=self.colores['texto_principal'])
        self.label_algoritmo.pack(anchor=tk.W)
        
        self.label_tiempo = tk.Label(frame_algoritmo, text="Tiempo Actual: 0", 
                                    font=("Segoe UI", 11), 
                                    bg=self.colores['fondo_secundario'],
                                    fg=self.colores['texto_secundario'])
        self.label_tiempo.pack(anchor=tk.W, pady=(5, 0))
        
        self.label_proceso_actual = tk.Label(frame_algoritmo, text="Proceso Actual: Ninguno", 
                                           font=("Segoe UI", 11), 
                                           bg=self.colores['fondo_secundario'],
                                           fg=self.colores['texto_secundario'])
        self.label_proceso_actual.pack(anchor=tk.W, pady=(5, 0))
        
        # Estadísticas
        frame_stats = tk.LabelFrame(frame_info, text="📊 Estadísticas", 
                                   font=("Segoe UI", 12, "bold"), 
                                   bg=self.colores['fondo_terciario'],
                                   fg=self.colores['texto_acento'],
                                   relief=tk.FLAT)
        frame_stats.pack(fill=tk.X, padx=15, pady=10)
        
        self.label_stats = tk.Label(frame_stats, text="", font=("Segoe UI", 10), 
                                   bg=self.colores['fondo_terciario'],
                                   fg=self.colores['texto_principal'], 
                                   justify=tk.LEFT)
        self.label_stats.pack(pady=10, padx=10)
        
        # Log de eventos
        frame_log = tk.LabelFrame(frame_info, text="📝 Log de Eventos", 
                                 font=("Segoe UI", 12, "bold"), 
                                 bg=self.colores['fondo_terciario'],
                                 fg=self.colores['texto_acento'],
                                 relief=tk.FLAT)
        frame_log.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        self.text_log = tk.Text(frame_log, height=12, font=("Consolas", 9), 
                               bg=self.colores['fondo_principal'], 
                               fg=self.colores['texto_principal'],
                               insertbackground=self.colores['texto_acento'],
                               selectbackground=self.colores['tabla_seleccion'],
                               relief=tk.FLAT, bd=0)
        scrollbar_log = ttk.Scrollbar(frame_log, orient=tk.VERTICAL, command=self.text_log.yview)
        self.text_log.configure(yscrollcommand=scrollbar_log.set)
        
        self.text_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar_log.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
    
    def cambiar_algoritmo(self, event=None):
        """Cambia el algoritmo de planificación"""
        self.simulador.algoritmo_actual = self.var_algoritmo.get()
        self.label_algoritmo.config(text=f"Algoritmo: {self.simulador.algoritmo_actual}")
        self.log_evento(f"Algoritmo cambiado a: {self.simulador.algoritmo_actual}")
    
    def ejecutar_simulacion(self):
        """Inicia la ejecución de la simulación en un hilo separado"""
        if self.simulador.ejecutando:
            messagebox.showwarning("Advertencia", "La simulación ya está en ejecución")
            return
        
        self.simulador.quantum = int(self.var_quantum.get())
        self.log_evento("=== INICIANDO SIMULACIÓN ===")
        self.log_evento(f"Algoritmo: {self.simulador.algoritmo_actual}")
        if self.simulador.algoritmo_actual == "Round Robin":
            self.log_evento(f"Quantum: {self.simulador.quantum}")
        
        # Ejecutar en hilo separado para no bloquear la interfaz
        thread = threading.Thread(target=self.simulador.ejecutar_simulacion, 
                                 args=(self.actualizar_interfaz,))
        thread.daemon = True
        thread.start()
    
    def resetear_simulacion(self):
        """Resetea la simulación"""
        self.simulador.resetear_simulacion()
        self.actualizar_tabla()
        self.actualizar_informacion()
        self.log_evento("=== SIMULACIÓN RESETEADA ===")
    
    def crear_procesos_nuevos(self):
        """Crea nuevos procesos de ejemplo"""
        self.simulador.crear_procesos_ejemplo()
        self.actualizar_tabla()
        self.log_evento("Procesos de ejemplo creados")
    
    def actualizar_interfaz(self):
        """Actualiza la interfaz durante la simulación"""
        self.ventana.after(0, self.actualizar_tabla)
        self.ventana.after(0, self.actualizar_informacion)
    
    def actualizar_tabla(self):
        """Actualiza la tabla de procesos con tema oscuro"""
        # Limpiar tabla
        for item in self.tabla_procesos.get_children():
            self.tabla_procesos.delete(item)
        
        # Agregar procesos
        for proceso in self.simulador.procesos + self.simulador.procesos_terminados:
            estado_color = self.obtener_color_estado(proceso.estado)
            
            self.tabla_procesos.insert("", "end", values=(
                proceso.id,
                proceso.nombre,
                proceso.tipo.value,
                proceso.tiempo_irrupcion,
                proceso.tiempo_ejecucion,
                proceso.prioridad_alerta,
                proceso.tamaño_datos,
                proceso.estado.value,
                proceso.tiempo_restante,
                proceso.tiempo_espera
            ), tags=(estado_color,))
        
        # Configurar colores del tema oscuro
        self.tabla_procesos.tag_configure("Nuevo", background=self.colores['nuevo'], foreground='white')
        self.tabla_procesos.tag_configure("Listo", background=self.colores['listo'], foreground='black')
        self.tabla_procesos.tag_configure("En Ejecución", background=self.colores['ejecucion'], foreground='white')
        self.tabla_procesos.tag_configure("Bloqueado", background=self.colores['bloqueado'], foreground='white')
        self.tabla_procesos.tag_configure("Terminado", background=self.colores['terminado'], foreground='white')
    
    def obtener_color_estado(self, estado):
        """Obtiene el color correspondiente al estado del proceso"""
        colores = {
            EstadoProceso.NUEVO: "Nuevo",
            EstadoProceso.LISTO: "Listo",
            EstadoProceso.EN_EJECUCION: "En Ejecución",
            EstadoProceso.BLOQUEADO: "Bloqueado",
            EstadoProceso.TERMINADO: "Terminado"
        }
        return colores.get(estado, "Nuevo")
    
    def actualizar_informacion(self):
        """Actualiza la información de simulación con tema oscuro"""
        self.label_tiempo.config(text=f"Tiempo Actual: {self.simulador.tiempo_actual}")
        
        if self.simulador.proceso_actual:
            self.label_proceso_actual.config(
                text=f"Proceso Actual: {self.simulador.proceso_actual.nombre}",
                fg=self.colores['texto_acento']
            )
        else:
            self.label_proceso_actual.config(text="Proceso Actual: Ninguno", 
                                           fg=self.colores['texto_secundario'])
        
        # Calcular estadísticas
        procesos_terminados = len(self.simulador.procesos_terminados)
        total_procesos = len(self.simulador.procesos)
        
        if procesos_terminados > 0:
            tiempo_promedio_espera = sum(p.tiempo_espera for p in self.simulador.procesos_terminados) / procesos_terminados
            tiempo_promedio_respuesta = sum(p.tiempo_respuesta for p in self.simulador.procesos_terminados) / procesos_terminados
            
            stats_text = f"""📊 Procesos Terminados: {procesos_terminados}/{total_procesos}
⏱️ Tiempo Promedio de Espera: {tiempo_promedio_espera:.2f}
🔄 Tiempo Promedio de Respuesta: {tiempo_promedio_respuesta:.2f}
⏰ Tiempo Total de Simulación: {self.simulador.tiempo_actual}"""
        else:
            stats_text = f"""📊 Procesos Terminados: {procesos_terminados}/{total_procesos}
⏰ Tiempo de Simulación: {self.simulador.tiempo_actual}"""
        
        self.label_stats.config(text=stats_text)
    
    def log_evento(self, mensaje):
        """Agrega un mensaje al log de eventos"""
        timestamp = time.strftime("%H:%M:%S")
        self.text_log.insert(tk.END, f"[{timestamp}] {mensaje}\n")
        self.text_log.see(tk.END)
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()

if __name__ == "__main__":
    app = InterfazSimulador()
    app.ejecutar()
