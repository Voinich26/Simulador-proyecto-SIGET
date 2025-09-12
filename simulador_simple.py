#!/usr/bin/env python3
"""
Versión simplificada del simulador SIGET para diagnóstico
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time

def crear_ventana_simple():
    """Crea una ventana simple para probar que tkinter funciona"""
    print("🎯 Creando ventana del simulador...")
    
    # Crear ventana principal
    root = tk.Tk()
    root.title("Simulador SIGET - Versión Simple")
    root.geometry("800x600")
    root.configure(bg='#f0f0f0')
    
    # Título
    titulo = tk.Label(root, text="🚦 Simulador SIGET - Funcionando!", 
                     font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
    titulo.pack(pady=20)
    
    # Información
    info = tk.Label(root, text="¡Python y tkinter están funcionando correctamente!", 
                   font=("Arial", 12), bg='#f0f0f0', fg='#27ae60')
    info.pack(pady=10)
    
    # Lista de procesos
    frame_procesos = tk.LabelFrame(root, text="Procesos del SIGET", 
                                  font=("Arial", 12, "bold"), bg='#f0f0f0')
    frame_procesos.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
    # Crear tabla simple
    columnas = ("ID", "Nombre", "Tipo", "Estado")
    tabla = ttk.Treeview(frame_procesos, columns=columnas, show="headings", height=10)
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150, anchor=tk.CENTER)
    
    # Agregar datos de ejemplo
    procesos_ejemplo = [
        (1, "Monitoreo Centro", "Tráfico", "Nuevo"),
        (2, "Semaforos Principal", "Semáforos", "Nuevo"),
        (3, "Análisis Patrones", "Datos", "Nuevo"),
        (4, "Monitoreo Periferia", "Tráfico", "Nuevo"),
        (5, "Semaforos Intersección", "Semáforos", "Nuevo"),
        (6, "Reporte Estadísticas", "Datos", "Nuevo")
    ]
    
    for proceso in procesos_ejemplo:
        tabla.insert("", "end", values=proceso)
    
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Botones
    frame_botones = tk.Frame(root, bg='#f0f0f0')
    frame_botones.pack(pady=20)
    
    def simular_cambio():
        """Simula un cambio de estado"""
        print("🔄 Simulando cambio de estado...")
        messagebox.showinfo("Simulación", "¡Los procesos están cambiando de estado!")
    
    def cerrar():
        """Cierra la aplicación"""
        print("👋 Cerrando simulador...")
        root.destroy()
    
    btn_simular = tk.Button(frame_botones, text="🔄 Simular Cambio", 
                           command=simular_cambio, bg='#3498db', fg='white',
                           font=("Arial", 12, "bold"), padx=20)
    btn_simular.pack(side=tk.LEFT, padx=10)
    
    btn_cerrar = tk.Button(frame_botones, text="❌ Cerrar", 
                          command=cerrar, bg='#e74c3c', fg='white',
                          font=("Arial", 12, "bold"), padx=20)
    btn_cerrar.pack(side=tk.LEFT, padx=10)
    
    # Información de estado
    estado = tk.Label(root, text="✅ Simulador funcionando correctamente", 
                     font=("Arial", 10), bg='#f0f0f0', fg='#27ae60')
    estado.pack(pady=10)
    
    print("✅ Ventana creada exitosamente")
    return root

def main():
    """Función principal"""
    print("🚀 Iniciando simulador simple...")
    
    try:
        # Crear y mostrar ventana
        root = crear_ventana_simple()
        print("🎯 Mostrando ventana...")
        root.mainloop()
        print("✅ Simulador cerrado correctamente")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()


