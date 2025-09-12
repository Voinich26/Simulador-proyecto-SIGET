#!/usr/bin/env python3
"""
Script de prueba simple para verificar Python
"""

print("🐍 ¡Python está funcionando!")
print("✅ Versión de Python detectada")

try:
    import tkinter as tk
    print("✅ tkinter está disponible")
    
    # Crear una ventana de prueba
    root = tk.Tk()
    root.title("Prueba de Python")
    root.geometry("300x200")
    
    label = tk.Label(root, text="¡Python y tkinter funcionan correctamente!", 
                    font=("Arial", 12), fg="green")
    label.pack(pady=50)
    
    button = tk.Button(root, text="Cerrar", command=root.destroy, 
                      bg="blue", fg="white", font=("Arial", 10))
    button.pack(pady=20)
    
    print("🎯 Abriendo ventana de prueba...")
    root.mainloop()
    
except ImportError as e:
    print(f"❌ Error con tkinter: {e}")
    print("💡 tkinter debería estar incluido con Python")
except Exception as e:
    print(f"❌ Error: {e}")

print("🏁 Prueba completada")


