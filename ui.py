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
    return tab


def tab_reservas(notebook, sistema):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Reservas")
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



