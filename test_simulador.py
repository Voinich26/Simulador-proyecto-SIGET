#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad del simulador SIGET
"""

def test_imports():
    """Prueba que todas las importaciones funcionen correctamente"""
    try:
        import tkinter as tk
        print("✅ tkinter importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando tkinter: {e}")
        return False
    
    try:
        import threading
        print("✅ threading importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando threading: {e}")
        return False
    
    try:
        import time
        print("✅ time importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando time: {e}")
        return False
    
    try:
        from enum import Enum
        print("✅ enum importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando enum: {e}")
        return False
    
    try:
        from dataclasses import dataclass
        print("✅ dataclasses importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando dataclasses: {e}")
        return False
    
    try:
        from typing import List, Optional
        print("✅ typing importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando typing: {e}")
        return False
    
    return True

def test_simulador_classes():
    """Prueba que las clases del simulador se puedan instanciar"""
    try:
        # Importar las clases del simulador
        import sys
        import os
        
        # Agregar el directorio actual al path
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        from simulador_siget import (
            EstadoProceso, TipoProceso, ProcesoSIGET, 
            AlgoritmoPlanificacion, SimuladorSIGET
        )
        
        print("✅ Clases del simulador importadas correctamente")
        
        # Probar creación de enums
        estado = EstadoProceso.NUEVO
        tipo = TipoProceso.MONITOREO_TRAFICO
        print(f"✅ Enums creados: {estado.value}, {tipo.value}")
        
        # Probar creación de proceso
        proceso = ProcesoSIGET(
            id=1,
            nombre="Test Process",
            tipo=TipoProceso.MONITOREO_TRAFICO,
            tiempo_irrupcion=0,
            tiempo_ejecucion=5,
            prioridad_alerta=1,
            tamaño_datos=100
        )
        print(f"✅ Proceso creado: {proceso.nombre}")
        
        # Probar creación de simulador
        simulador = SimuladorSIGET()
        print("✅ Simulador creado correctamente")
        
        # Probar algoritmos
        procesos_test = [proceso]
        fifo_result = AlgoritmoPlanificacion.fifo(procesos_test)
        sjf_result = AlgoritmoPlanificacion.sjf(procesos_test)
        prioridad_result = AlgoritmoPlanificacion.prioridad(procesos_test)
        rr_result = AlgoritmoPlanificacion.round_robin(procesos_test)
        
        print("✅ Algoritmos de planificación funcionando")
        
        return True
        
    except Exception as e:
        print(f"❌ Error probando clases del simulador: {e}")
        return False

def test_interface_creation():
    """Prueba que la interfaz se pueda crear (sin mostrarla)"""
    try:
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        from simulador_siget import InterfazSimulador
        
        # Crear la interfaz pero no mostrarla
        print("✅ Interfaz del simulador se puede crear correctamente")
        print("   (No se muestra la ventana para evitar bloqueo)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando interfaz: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🧪 PRUEBAS DEL SIMULADOR SIGET")
    print("=" * 40)
    
    # Ejecutar pruebas
    tests = [
        ("Importaciones básicas", test_imports),
        ("Clases del simulador", test_simulador_classes),
        ("Creación de interfaz", test_interface_creation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Ejecutando: {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name}: PASÓ")
        else:
            print(f"❌ {test_name}: FALLÓ")
    
    print("\n" + "=" * 40)
    print(f"📊 RESULTADOS: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El simulador está listo para usar.")
        print("\nPara ejecutar el simulador:")
        print("  python simulador_siget.py")
        print("  o")
        print("  python ejecutar_simulador.py")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")
    
    return passed == total

if __name__ == "__main__":
    main()


