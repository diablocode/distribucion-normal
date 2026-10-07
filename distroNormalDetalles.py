import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import norm


# ============================================================
# FUNCIONES ESTADÍSTICAS
# ============================================================

def actualizar():

    try:
        # ----------------------------------------------------
        # Obtener valores introducidos por el usuario
        # ----------------------------------------------------

        mu = float(entry_media.get())
        sigma = float(entry_sigma.get())
        limite_inferior = float(entry_inferior.get())
        limite_superior = float(entry_superior.get())

        # ----------------------------------------------------
        # Validaciones
        # ----------------------------------------------------

        if sigma <= 0:
            messagebox.showerror(
                "Error",
                "La desviación estándar debe ser mayor que 0."
            )
            return

        if limite_inferior >= limite_superior:
            messagebox.showerror(
                "Error",
                "El límite inferior debe ser menor que el límite superior."
            )
            return

        # ----------------------------------------------------
        # Crear distribución
        # ----------------------------------------------------

        x = np.linspace(
            mu - 4 * sigma,
            mu + 4 * sigma,
            1000
        )

        y = norm.pdf(x, mu, sigma)

        # ----------------------------------------------------
        # Probabilidad entre los límites
        # ----------------------------------------------------

        probabilidad = (
            norm.cdf(limite_superior, mu, sigma)
            -
            norm.cdf(limite_inferior, mu, sigma)
        )

        # ----------------------------------------------------
        # Estadísticos de una distribución normal
        # ----------------------------------------------------

        media = mu

        mediana = mu

        moda = mu

        varianza = sigma ** 2

        desviacion = sigma

        # Curtosis de Fisher de una distribución normal
        curtosis = 0

        # Si usamos curtosis de Pearson sería 3
        curtosis_pearson = 3

        asimetria = 0

        # ----------------------------------------------------
        # Actualizar valores en pantalla
        # ----------------------------------------------------

        valor_media.set(f"{media:.4f}")
        valor_mediana.set(f"{mediana:.4f}")
        valor_moda.set(f"{moda:.4f}")
        valor_varianza.set(f"{varianza:.4f}")
        valor_desviacion.set(f"{desviacion:.4f}")
        valor_curtosis.set(f"{curtosis:.4f}")
        valor_asimetria.set(f"{asimetria:.4f}")

        valor_probabilidad.set(
            f"{probabilidad:.6f}  ({probabilidad * 100:.2f} %)"
        )

        # ----------------------------------------------------
        # Limpiar gráfica anterior
        # ----------------------------------------------------

        ax.clear()

        # ----------------------------------------------------
        # Dibujar campana
        # ----------------------------------------------------

        ax.plot(
            x,
            y,
            linewidth=2,
            label="Distribución normal"
        )

        # ----------------------------------------------------
        # Área seleccionada
        # ----------------------------------------------------

        x_area = np.linspace(
            limite_inferior,
            limite_superior,
            500
        )

        y_area = norm.pdf(
            x_area,
            mu,
            sigma
        )

        ax.fill_between(
            x_area,
            y_area,
            alpha=0.35,
            label=f"Probabilidad = {probabilidad * 100:.2f}%"
        )

        # ----------------------------------------------------
        # Línea de la media
        # ----------------------------------------------------

        ax.axvline(
            mu,
            linestyle="--",
            linewidth=1.5,
            label=f"μ = {mu}"
        )

        # ----------------------------------------------------
        # Límites seleccionados
        # ----------------------------------------------------

        ax.axvline(
            limite_inferior,
            linestyle=":",
            linewidth=2
        )

        ax.axvline(
            limite_superior,
            linestyle=":",
            linewidth=2
        )

        # Texto de límites

        ax.text(
            limite_inferior,
            max(y) * 0.15,
            f"LI = {limite_inferior:.2f}",
            ha="right"
        )

        ax.text(
            limite_superior,
            max(y) * 0.15,
            f"LS = {limite_superior:.2f}",
            ha="left"
        )

        # ----------------------------------------------------
        # Líneas de desviación estándar
        # ----------------------------------------------------

        for z in [-3, -2, -1, 1, 2, 3]:

            valor = mu + z * sigma

            ax.axvline(
                valor,
                linestyle="--",
                alpha=0.25
            )

        # ----------------------------------------------------
        # Configuración gráfica
        # ----------------------------------------------------

        ax.set_title(
            "Distribución Normal",
            fontsize=16
        )

        ax.set_xlabel("Valores")
        ax.set_ylabel("Densidad de probabilidad")

        ax.grid(alpha=0.2)

        ax.legend()

        canvas.draw()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Introduce valores numéricos válidos."
        )


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

root = tk.Tk()

root.title(
    "Explorador de la Distribución Normal"
)

root.geometry("1200x750")


# ============================================================
# FRAME DE PARÁMETROS
# ============================================================

frame_parametros = ttk.LabelFrame(
    root,
    text="Parámetros de la distribución",
    padding=10
)

frame_parametros.pack(
    side=tk.TOP,
    fill=tk.X,
    padx=10,
    pady=10
)


# ------------------------------------------------------------
# Media
# ------------------------------------------------------------

ttk.Label(
    frame_parametros,
    text="Media (μ):"
).grid(row=0, column=0, padx=5, pady=5)

entry_media = ttk.Entry(
    frame_parametros,
    width=12
)

entry_media.insert(0, "100")

entry_media.grid(
    row=0,
    column=1,
    padx=5
)


# ------------------------------------------------------------
# Desviación estándar
# ------------------------------------------------------------

ttk.Label(
    frame_parametros,
    text="Desviación estándar (σ):"
).grid(row=0, column=2, padx=5)

entry_sigma = ttk.Entry(
    frame_parametros,
    width=12
)

entry_sigma.insert(0, "15")

entry_sigma.grid(
    row=0,
    column=3,
    padx=5
)


# ------------------------------------------------------------
# Límite inferior
# ------------------------------------------------------------

ttk.Label(
    frame_parametros,
    text="Límite inferior:"
).grid(row=1, column=0, padx=5, pady=5)

entry_inferior = ttk.Entry(
    frame_parametros,
    width=12
)

entry_inferior.insert(0, "85")

entry_inferior.grid(
    row=1,
    column=1,
    padx=5
)


# ------------------------------------------------------------
# Límite superior
# ------------------------------------------------------------

ttk.Label(
    frame_parametros,
    text="Límite superior:"
).grid(row=1, column=2, padx=5)

entry_superior = ttk.Entry(
    frame_parametros,
    width=12
)

entry_superior.insert(0, "115")

entry_superior.grid(
    row=1,
    column=3,
    padx=5
)


# ------------------------------------------------------------
# Botón actualizar
# ------------------------------------------------------------

boton = ttk.Button(
    frame_parametros,
    text="Actualizar distribución",
    command=actualizar
)

boton.grid(
    row=0,
    column=4,
    rowspan=2,
    padx=20
)


# ============================================================
# FRAME ESTADÍSTICAS
# ============================================================

frame_estadisticas = ttk.LabelFrame(
    root,
    text="Valores estadísticos",
    padding=10
)

frame_estadisticas.pack(
    side=tk.LEFT,
    fill=tk.Y,
    padx=10,
    pady=10
)


# Variables de Tkinter

valor_media = tk.StringVar()
valor_mediana = tk.StringVar()
valor_moda = tk.StringVar()
valor_varianza = tk.StringVar()
valor_desviacion = tk.StringVar()
valor_curtosis = tk.StringVar()
valor_asimetria = tk.StringVar()
valor_probabilidad = tk.StringVar()


# ------------------------------------------------------------
# Función para crear filas
# ------------------------------------------------------------

def crear_fila(
    fila,
    nombre,
    variable
):

    ttk.Label(
        frame_estadisticas,
        text=nombre
    ).grid(
        row=fila,
        column=0,
        sticky="w",
        padx=5,
        pady=6
    )

    ttk.Label(
        frame_estadisticas,
        textvariable=variable,
        font=("Arial", 10, "bold")
    ).grid(
        row=fila,
        column=1,
        sticky="e",
        padx=5
    )


crear_fila(
    0,
    "Media:",
    valor_media
)

crear_fila(
    1,
    "Mediana:",
    valor_mediana
)

crear_fila(
    2,
    "Moda:",
    valor_moda
)

crear_fila(
    3,
    "Varianza:",
    valor_varianza
)

crear_fila(
    4,
    "Desviación estándar:",
    valor_desviacion
)

crear_fila(
    5,
    "Curtosis:",
    valor_curtosis
)

crear_fila(
    6,
    "Asimetría:",
    valor_asimetria
)


# ============================================================
# PROBABILIDAD
# ============================================================

frame_probabilidad = ttk.LabelFrame(
    frame_estadisticas,
    text="Área seleccionada",
    padding=10
)

frame_probabilidad.grid(
    row=8,
    column=0,
    columnspan=2,
    pady=20
)

ttk.Label(
    frame_probabilidad,
    text="P(LI ≤ X ≤ LS)"
).pack()

ttk.Label(
    frame_probabilidad,
    textvariable=valor_probabilidad,
    font=("Arial", 14, "bold")
).pack(
    pady=10
)


# ============================================================
# GRÁFICA
# ============================================================

frame_grafica = ttk.Frame(root)

frame_grafica.pack(
    side=tk.RIGHT,
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=10
)


fig, ax = plt.subplots(
    figsize=(8, 6)
)

canvas = FigureCanvasTkAgg(
    fig,
    master=frame_grafica
)

canvas.get_tk_widget().pack(
    fill=tk.BOTH,
    expand=True
)


# ============================================================
# EJECUTAR AL INICIO
# ============================================================

actualizar()

root.mainloop()