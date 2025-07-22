import tkinter as tk
from view.productos_view import cargar_productos
from view.agregar_view import agregar_productos

def ventana_usuario(datos):
    """
    Crea la ventana principal del dashboard después del login
    
    Args:
        datos: Parámetro no utilizado actualmente
    """
    # Configuración de la ventana
    venta_usuario = tk.Tk()
    venta_usuario.title("Panel de Administración - Mi Tienda")
    venta_usuario.geometry("1100x600")
    venta_usuario.minsize(1000, 500)
    
    # Configuración del grid para responsive design
    venta_usuario.grid_rowconfigure(0, weight=1)
    venta_usuario.grid_columnconfigure(1, weight=1)
    
    # Frame principal
    main_frame = tk.Frame(venta_usuario)
    main_frame.pack(fill="both", expand=True)
    
    # Panel izquierdo para agregar productos
    agregar_frame = tk.Frame(main_frame, width=250, bg="white")
    agregar_frame.pack(side="left", fill="y")
    agregar_productos(agregar_frame)  # Carga el módulo de agregar productos
    
    # Panel derecho para listar productos
    productos_frame = tk.Frame(main_frame, bg="#f5f7fa")
    productos_frame.pack(side="right", fill="both", expand=True)
    cargar_productos(productos_frame)  # Carga el módulo de listar productos
    
    # Inicia el bucle principal
    venta_usuario.mainloop()