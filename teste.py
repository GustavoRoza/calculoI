import plotly.express as px
import pandas as pd
import tkinter as tk
from tkinter import ttk
import tempfile
import os
import webbrowser


def gerar_grafico():
    try:
        a = float(eval(entry_a.get()))
        b = float(eval(entry_b.get()))
        c = float(eval(entry_c.get()))
        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())

        # Calcular pontos mais densos (passo de 0.1)
        x = [round(i, 1) for i in frange(x_min, x_max, 0.1)]
        y = [a * (xi ** 2) + b * xi + c for xi in x]
        df = pd.DataFrame({"x": x, "y": y})

        # Criar gráfico
        fig = px.line(df, x="x", y="y", title=f"y = {a}x² + {b}x + {c}",
                      markers=True)  # sem marcadores para ficar suave
        fig.update_traces(line=dict(color="royalblue", width=2))
        fig.update_layout(
            plot_bgcolor="#f7f7f7",
            xaxis_title="eixo X",
            yaxis_title="eixo Y",
            hovermode="x unified",  # mostra x e y unificados
            title_font=dict(size=14, family="Arial", color="black")
        )

        # Adicionar linhas dos eixos
        fig.add_hline(y=0, line_width=1, line_color="black")
        fig.add_vline(x=0, line_width=1, line_color="black")

        # Salvar e abrir no navegador
        temp_html = os.path.join(tempfile.gettempdir(), "grafico.html")
        fig.write_html(temp_html, include_plotlyjs="cdn")
        webbrowser.open(f"file://{temp_html}")

        lbl_status.config(text="✅ Gráfico aberto no navegador!", foreground="green")
    except ValueError:
        lbl_status.config(text="❌ Valores inválidos", foreground="red")


# Função auxiliar para gerar range com passo decimal
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step


# Criar janela principal
calculadora = tk.Tk()
calculadora.title("Calculadora de equação quadrática")

# Centralizar janela
largura_janela = 500
altura_janela = 250
largura_tela = calculadora.winfo_screenwidth()
altura_tela = calculadora.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (largura_janela // 2)
calculadora.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

texto = tk.Label(
    calculadora,
    text="Uma expressão quadrática possui o seguinte formato: ",
    font=("Arial", 10)
)
texto.pack()
texto_exp = tk.Label(
    calculadora,
    text="y = ax² + bx + c",
    font=("Arial", 10, "italic")
)
texto_exp.pack()

texto_exp = tk.Label(
    calculadora,
    text="onde a, b e c são constantes pertencentes aos números reais (R).",
    font=("Arial", 10)
)
texto_exp.pack()
# Frame para entradas
frame_inputs = ttk.Frame(calculadora, padding=10)
frame_inputs.pack(fill="x")

ttk.Label(frame_inputs, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = ttk.Entry(frame_inputs, width=10)
entry_a.grid(row=0, column=1)
entry_a.insert(0, "")

ttk.Label(frame_inputs, text="b:").grid(row=0, column=2, padx=5, pady=5)
entry_b = ttk.Entry(frame_inputs, width=10)
entry_b.grid(row=0, column=3)
entry_b.insert(0, "")

ttk.Label(frame_inputs, text="c:").grid(row=0, column=4, padx=5, pady=5)
entry_c = ttk.Entry(frame_inputs, width=10)
entry_c.grid(row=0, column=5)
entry_c.insert(0, "")

ttk.Label(frame_inputs, text="x mínimo:").grid(row=1, column=0, padx=5, pady=5)
entry_xmin = ttk.Entry(frame_inputs, width=10)
entry_xmin.grid(row=1, column=1)
entry_xmin.insert(0, "")

ttk.Label(frame_inputs, text="x máximo:").grid(row=1, column=2, padx=5, pady=5)
entry_xmax = ttk.Entry(frame_inputs, width=10)
entry_xmax.grid(row=1, column=3)
entry_xmax.insert(0, "")

# Botão
btn_plot = ttk.Button(frame_inputs, text="Gerar Gráfico", command=gerar_grafico)
btn_plot.grid(row=2, column=0, columnspan=6, pady=10)

# Status
lbl_status = ttk.Label(calculadora, text="")
lbl_status.pack()

calculadora.mainloop()
