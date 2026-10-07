import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ==========================================
# DISTRIBUCIÓN NORMAL
# ==========================================

def explicar_distribucion_normal(mu=0, sigma=1):

    # Valores del eje X
    x = np.linspace(mu - 4 * sigma,
                    mu + 4 * sigma,
                    1000)

    # Función de densidad normal
    y = norm.pdf(x, mu, sigma)

    # Crear gráfica
    plt.figure(figsize=(12, 7))

    plt.plot(x, y, linewidth=2,
             label=f"N({mu}, {sigma}²)")

    # ------------------------------------------
    # Zonas de desviación estándar
    # ------------------------------------------

    colores = [
        (-3, 3, "±3σ"),
        (-2, 2, "±2σ"),
        (-1, 1, "±1σ")
    ]

    # Sombras para las diferentes zonas
    for izquierda, derecha, etiqueta in colores:

        x_fill = np.linspace(
            mu + izquierda * sigma,
            mu + derecha * sigma,
            500
        )

        y_fill = norm.pdf(x_fill, mu, sigma)

        plt.fill_between(
            x_fill,
            y_fill,
            alpha=0.15,
            label=etiqueta
        )

    # ------------------------------------------
    # Líneas de desviación estándar
    # ------------------------------------------

    for z in [-3, -2, -1, 0, 1, 2, 3]:

        valor = mu + z * sigma

        plt.axvline(
            valor,
            linestyle="--",
            alpha=0.6
        )

        if z == 0:
            texto = f"μ = {valor:.1f}"
        else:
            texto = f"{z:+}σ\n{valor:.1f}"

        plt.text(
            valor,
            max(y) * 0.05,
            texto,
            ha="center"
        )

    # ------------------------------------------
    # Títulos y etiquetas
    # ------------------------------------------

    plt.title(
        "Distribución Normal",
        fontsize=18
    )

    plt.xlabel("Valor")
    plt.ylabel("Densidad de probabilidad")

    plt.grid(alpha=0.2)

    plt.legend()

    plt.tight_layout()

    plt.show()


# ==========================================
# EJEMPLO
# ==========================================

explicar_distribucion_normal(
    mu=100,
    sigma=15
)