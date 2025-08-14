import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def gerar_grafico():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        x_min = int(entry_xmin.get())
        x_max = int(entry_xmax.get())

        # Calcular pontos
        x = list(range(x_min, x_max + 1))
        y = [a * (xi ** 2) + b * xi + c for xi in x]

        # Limpar gráfico anterior
        ax.clear()

        # Fundo
        ax.set_facecolor("#f7f7f7")

        # Plot com estilo
        ax.plot(x, y, color="royalblue", linewidth=2, marker="o", markersize=6, markerfacecolor="orange")

        # Linhas centrais nos eixos
        ax.axhline(0, color="black", linewidth=1)
        ax.axvline(0, color="black", linewidth=1)

        # Título e labels
        ax.set_title(f"Gráfico: y = {a}x² + {b}x + {c}", fontsize=12, fontweight="bold")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        # Grid suave
        ax.grid(True, linestyle="--", alpha=0.6)

        canvas.draw()
        lbl_status.config(text="✅ Gráfico gerado com sucesso!", foreground="green")
    except ValueError:
        lbl_status.config(text="❌ Valores inválidos", foreground="red")


# Criar janela principal
root = tk.Tk()
root.title("Equação Quadrática")

# Centralizar janela
largura_janela = 650
altura_janela = 550
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Frame para entradas
frame_inputs = ttk.Frame(root, padding=10)
frame_inputs.pack(fill="x")

# Exemplo de equação
ttk.Label(frame_inputs, text="Formato: y = ax² + bx + c", font=("Arial", 10, "italic")).grid(row=0, column=0, columnspan=6, pady=5)
ttk.Label(frame_inputs, text="(Ex: y = 1x² - 4x + 3)", font=("Arial", 9)).grid(row=1, column=0, columnspan=6, pady=(0, 10))

# Campos
ttk.Label(frame_inputs, text="a:").grid(row=2, column=0, padx=5, pady=5)
entry_a = ttk.Entry(frame_inputs, width=10)
entry_a.grid(row=2, column=1, padx=5, pady=5)
entry_a.insert(0, "1")

ttk.Label(frame_inputs, text="b:").grid(row=2, column=2, padx=5, pady=5)
entry_b = ttk.Entry(frame_inputs, width=10)
entry_b.grid(row=2, column=3, padx=5, pady=5)
entry_b.insert(0, "-4")

ttk.Label(frame_inputs, text="c:").grid(row=2, column=4, padx=5, pady=5)
entry_c = ttk.Entry(frame_inputs, width=10)
entry_c.grid(row=2, column=5, padx=5, pady=5)
entry_c.insert(0, "3")

ttk.Label(frame_inputs, text="x mínimo:").grid(row=3, column=0, padx=5, pady=5)
entry_xmin = ttk.Entry(frame_inputs, width=10)
entry_xmin.grid(row=3, column=1, padx=5, pady=5)
entry_xmin.insert(0, "-5")

ttk.Label(frame_inputs, text="x máximo:").grid(row=3, column=2, padx=5, pady=5)
entry_xmax = ttk.Entry(frame_inputs, width=10)
entry_xmax.grid(row=3, column=3, padx=5, pady=5)
entry_xmax.insert(0, "7")

# Botão para gerar gráfico
btn_plot = ttk.Button(frame_inputs, text="Gerar Gráfico", command=gerar_grafico)
btn_plot.grid(row=4, column=0, columnspan=6, pady=10)

# Label de status
lbl_status = ttk.Label(root, text="")
lbl_status.pack()

# Criar figura do matplotlib dentro da janela
fig, ax = plt.subplots(figsize=(5.5, 3.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True)

root.mainloop()
