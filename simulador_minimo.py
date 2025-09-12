#!/usr/bin/env python3
"""
Simulador mínimo para verificar que la interfaz gráfica funciona
"""

import tkinter as tk
from tkinter import ttk
import time

def main():
    print("🚀 Iniciando simulador mínimo...")
    
    try:
        # Crear ventana principal
        root = tk.Tk()
        root.title("Simulador SIGET - Versión Mínima")
        root.geometry("600x400")
        root.configure(bg='#f0f0f0')
        
        print("✅ Ventana creada")
        
        # Título
        titulo = tk.Label(root, text="🚦 SIMULADOR SIGET FUNCIONANDO!", 
                         font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=20)
        
        print("✅ Título agregado")
        
        # Información
        info = tk.Label(root, text="¡La interfaz gráfica está funcionando correctamente!", 
                       font=("Arial", 12), bg='#f0f0f0', fg='#27ae60')
        info.pack(pady=10)
        
        print("✅ Información agregada")
        
        # Tabla simple
        frame_tabla = tk.LabelFrame(root, text="Procesos del SIGET", 
                                   font=("Arial", 12, "bold"), bg='#f0f0f0')
        frame_tabla.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Crear tabla
        columnas = ("ID", "Nombre", "Tipo", "Estado")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120, anchor=tk.CENTER)
        
        # Agregar datos
        procesos = [
            (1, "Monitoreo Centro", "Tráfico", "Nuevo"),
            (2, "Semaforos Principal", "Semáforos", "Nuevo"),
            (3, "Análisis Patrones", "Datos", "Nuevo"),
            (4, "Monitoreo Periferia", "Tráfico", "Nuevo"),
            (5, "Semaforos Intersección", "Semáforos", "Nuevo"),
            (6, "Reporte Estadísticas", "Datos", "Nuevo")
        ]
        
        for proceso in procesos:
            tabla.insert("", "end", values=proceso)
        
        tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        print("✅ Tabla creada")
        
        # Botones
        frame_botones = tk.Frame(root, bg='#f0f0f0')
        frame_botones.pack(pady=20)
        
        def simular():
            print("🔄 Simulando...")
            info.config(text="¡Simulación en progreso!")
            root.after(2000, lambda: info.config(text="¡Simulación completada!"))
        
        def cerrar():
            print("👋 Cerrando...")
            root.destroy()
        
        btn_simular = tk.Button(frame_botones, text="🔄 Simular", 
                               command=simular, bg='#3498db', fg='white',
                               font=("Arial", 12, "bold"), padx=20)
        btn_simular.pack(side=tk.LEFT, padx=10)
        
        btn_cerrar = tk.Button(frame_botones, text="❌ Cerrar", 
                              command=cerrar, bg='#e74c3c', fg='white',
                              font=("Arial", 12, "bold"), padx=20)
        btn_cerrar.pack(side=tk.LEFT, padx=10)
        
        print("✅ Botones creados")
        
        # Estado
        estado = tk.Label(root, text="✅ Simulador funcionando correctamente", 
                         font=("Arial", 10), bg='#f0f0f0', fg='#27ae60')
        estado.pack(pady=10)
        
        print("✅ Estado agregado")
        print("🎯 Mostrando ventana...")
        
        # Mostrar ventana
        root.mainloop()
        
        print("✅ Simulador cerrado correctamente")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()


