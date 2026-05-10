import tkinter as tk
from tkinter import ttk
from errores import DatoInvalidoError, ReservaError
from sistema import Sistema
from reserva import Reserva
import entidades

def crear_sistema_con_datos_iniciales():
    sistema = Sistema()
    sistema.agregar_servicio(entidades.ServicioReservaSalas(sala_numero=101, precio_hora=50.0))
    sistema.agregar_servicio(entidades.ServicioAlquilerEquipos(equipo_tipo="Proyector", precio_hora=20.0))
    sistema.agregar_servicio(entidades.ServicioAsesoriasEspecializadas(especialidad="Matemáticas", precio_hora=100.0))
    sistema.agregar_cliente(entidades.Cliente("Juan Pérez", "12345678", "juan@gmail.com", "3111111111"))
    sistema.agregar_cliente(entidades.Cliente("María López", "87654321", "maria@gmail.com", "3222222222"))
    reserva_ejemplo = Reserva(sistema.clientes[0], sistema.servicios[0], duracion=2)
    sistema.realizar_reserva(reserva_ejemplo)
    return sistema


def tab_clientes(notebook, sistema):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Clientes")

    label = ttk.Label(tab, text="Lista de clientes")
    label.pack(anchor="w", padx=12, pady=(12, 4))

    listbox = tk.Listbox(tab, height=10)
    listbox.pack(fill="both", expand=True, padx=12, pady=4)

    def refresh_clientes():
        listbox.delete(0, "end")
        for cliente in sistema.clientes:
            listbox.insert("end", cliente.describir())

    form_frame = ttk.LabelFrame(tab, text="Agregar cliente")
    form_frame.pack(fill="x", padx=12, pady=8)

    nombre_var = tk.StringVar()
    documento_var = tk.StringVar()
    email_var = tk.StringVar()
    telefono_var = tk.StringVar()
    status_var = tk.StringVar()

    ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=nombre_var, width=30).grid(row=0, column=1, padx=4, pady=2)
    ttk.Label(form_frame, text="Documento:").grid(row=1, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=documento_var, width=30).grid(row=1, column=1, padx=4, pady=2)
    ttk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=email_var, width=30).grid(row=2, column=1, padx=4, pady=2)
    ttk.Label(form_frame, text="Teléfono:").grid(row=3, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=telefono_var, width=30).grid(row=3, column=1, padx=4, pady=2)

    status_label = ttk.Label(form_frame, textvariable=status_var, foreground="red")
    status_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=4, pady=2)

    def agregar_cliente():
        try:
            cliente = entidades.Cliente(
                nombre_var.get(),
                documento_var.get(),
                email_var.get(),
                telefono_var.get(),
            )
            sistema.agregar_cliente(cliente)
            refresh_clientes()                
            nombre_var.set("")
            documento_var.set("")
            email_var.set("")
            telefono_var.set("")
            status_var.set("Cliente agregado correctamente.")
        except DatoInvalidoError as err:
            status_var.set(str(err))

    ttk.Button(form_frame, text="Agregar cliente", command=agregar_cliente).grid(row=5, column=0, columnspan=2, pady=6)

    refresh_clientes()
    return tab


def tab_servicios(notebook, sistema):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Servicios")

    label = ttk.Label(tab, text="Lista de servicios")
    label.pack(anchor="w", padx=12, pady=(12, 4))

    listbox = tk.Listbox(tab, height=10)
    listbox.pack(fill="both", expand=True, padx=12, pady=4)

    def refresh_servicios():
        listbox.delete(0, "end")
        for servicio in sistema.servicios:
            listbox.insert("end", servicio.descripcion())
    form_frame = ttk.LabelFrame(tab, text="Agregar servicio")
    form_frame.pack(fill="x", padx=12, pady=8)

    
    tipo_var       = tk.StringVar()
    detalle_var    = tk.StringVar()
    precio_var     = tk.StringVar()
    status_var     = tk.StringVar()

    
    ttk.Label(form_frame, text="Tipo de servicio:").grid(row=0, column=0, sticky="w", padx=4, pady=2)
    tipo_combo = ttk.Combobox(form_frame, textvariable=tipo_var, width=28)
    tipo_combo["values"] = ["Reserva de Sala", "Alquiler de Equipo", "Asesoría Especializada"]
    tipo_combo.grid(row=0, column=1, padx=4, pady=2)

    
    ttk.Label(form_frame, text="Detalle:").grid(row=1, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=detalle_var, width=30).grid(row=1, column=1, padx=4, pady=2)

    
    ttk.Label(form_frame, text="Precio por hora:").grid(row=2, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=precio_var, width=30).grid(row=2, column=1, padx=4, pady=2)

    
    status_label = ttk.Label(form_frame, textvariable=status_var, foreground="red")
    status_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=4, pady=2)
    
    def agregar_servicio():
        try:
            tipo     = tipo_var.get()
            detalle  = detalle_var.get()
            precio   = float(precio_var.get())

            if not tipo:
                raise DatoInvalidoError("Seleccione un tipo de servicio.")
            if not detalle:
                raise DatoInvalidoError("El detalle no puede estar vacío.")
            if precio <= 0:
                raise DatoInvalidoError("El precio debe ser mayor a cero.")

            
            if tipo == "Reserva de Sala":
                servicio = entidades.ServicioReservaSalas(
                    sala_numero=detalle, precio_hora=precio
                )
            elif tipo == "Alquiler de Equipo":
                servicio = entidades.ServicioAlquilerEquipos(
                    equipo_tipo=detalle, precio_hora=precio
                )
            elif tipo == "Asesoría Especializada":
                servicio = entidades.ServicioAsesoriasEspecializadas(
                    especialidad=detalle, precio_hora=precio
                )

            sistema.agregar_servicio(servicio)
            refresh_servicios()

            
            tipo_var.set("")
            detalle_var.set("")
            precio_var.set("")
            status_var.set("✅ Servicio agregado correctamente.")

        except DatoInvalidoError as e:
            status_var.set(f"❌ {e}")
        except ValueError:
            status_var.set("❌ El precio debe ser un número.")

    ttk.Button(form_frame, text="Agregar servicio",
               command=agregar_servicio).grid(row=4, column=0,
               columnspan=2, pady=6)

    refresh_servicios()
    return tab

def tab_reservas(notebook, sistema):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Reservas")

    label = ttk.Label(tab, text="Lista de reservas")
    label.pack(anchor="w", padx=12, pady=(12, 4))

    listbox = tk.Listbox(tab, height=10)
    listbox.pack(fill="both", expand=True, padx=12, pady=4)

    def refresh_reservas():
        listbox.delete(0, "end")
        for reserva in sistema.reservas:
            listbox.insert("end", reserva.describir())
    form_frame = ttk.LabelFrame(tab, text="Agregar reserva")
    form_frame.pack(fill="x", padx=12, pady=8)

    cliente_var  = tk.StringVar()
    servicio_var = tk.StringVar()
    duracion_var = tk.StringVar()
    status_var   = tk.StringVar()
    
    ttk.Label(form_frame, text="Cliente:").grid(row=0, column=0, sticky="w", padx=4, pady=2)
    cliente_combo = ttk.Combobox(form_frame, textvariable=cliente_var, width=28)
    cliente_combo.grid(row=0, column=1, padx=4, pady=2)


    ttk.Label(form_frame, text="Servicio:").grid(row=1, column=0, sticky="w", padx=4, pady=2)
    servicio_combo = ttk.Combobox(form_frame, textvariable=servicio_var, width=28)
    servicio_combo.grid(row=1, column=1, padx=4, pady=2)

    
    ttk.Label(form_frame, text="Duración (horas):").grid(row=2, column=0, sticky="w", padx=4, pady=2)
    ttk.Entry(form_frame, textvariable=duracion_var, width=30).grid(row=2, column=1, padx=4, pady=2)

    
    status_label = ttk.Label(form_frame, textvariable=status_var, foreground="red")
    status_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=4, pady=2)
    def agregar_reserva():
        try:
            
            cliente_nombre = cliente_var.get()
            cliente = next((c for c in sistema.clientes 
                          if c.nombre == cliente_nombre), None)
            if not cliente:
                raise DatoInvalidoError("Seleccione un cliente válido.")

            
            servicio_nombre = servicio_var.get()
            servicio = next((s for s in sistema.servicios 
                           if s.nombre == servicio_nombre), None)
            if not servicio:
                raise DatoInvalidoError("Seleccione un servicio válido.")

            
            duracion = float(duracion_var.get())

            
            reserva = Reserva(cliente, servicio, duracion)
            reserva.procesar()
            sistema.realizar_reserva(reserva)
            refresh_reservas()

            
            cliente_var.set("")
            servicio_var.set("")
            duracion_var.set("")
            status_var.set("✅ Reserva agregada correctamente.")

        except DatoInvalidoError as e:
            status_var.set(f"❌ {e}")
        except ReservaError as e:
            status_var.set(f"❌ {e}")
        except ValueError:
            status_var.set("❌ La duración debe ser un número.")

    
    cliente_combo["values"] = [c.nombre for c in sistema.clientes]
    servicio_combo["values"] = [s.nombre for s in sistema.servicios]


    ttk.Button(form_frame, text="Agregar reserva", 
               command=agregar_reserva).grid(row=4, column=0, 
               columnspan=2, pady=6)

    refresh_reservas()
    return tab

def crear_app():
    root = tk.Tk()
    root.title("Sistema de Reservas")
    root.geometry("800x600")

    sistema = crear_sistema_con_datos_iniciales()

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    tab_clientes(notebook, sistema)
    tab_servicios(notebook, sistema)
    tab_reservas(notebook, sistema)

    return root



