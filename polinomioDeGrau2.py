import plotly.express as px
import pandas as pd

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

a = 1
b = -5
c = 6
x_min = -10.0
x_max = 10.0
n = 2

nome_arquivo = "parabola.png" 

try:
    # Calcular os pontos da parábola
    x_vals = [round(i, 2) for i in frange(x_min, x_max, n)]
    y_vals = [a * (xi ** 2) + b * xi + c for xi in x_vals]
    
    # Criar o DataFrame e o gráfico
    df = pd.DataFrame({"x": x_vals, "y": y_vals})
    titulo = f"y = {a}x² + {b}x + {c}"    
    fig = px.line(df, x="x", y="y", title=titulo, markers=True) 
    fig.update_traces(line=dict(color="royalblue", width=2), marker=dict(size=8))
    fig.update_layout(
        plot_bgcolor="#f7f7f7",
        xaxis_title="Eixo X",
        yaxis_title="Eixo Y",
        hovermode="x unified",
        title_font=dict(size=14, family="Arial", color="black")
    )
    fig.add_hline(y=0, line_width=1, line_color="black")
    fig.add_vline(x=0, line_width=1, line_color="black")
    fig.write_image(nome_arquivo)
    print(f"✅ Gráfico gerado e salvo com sucesso como '{nome_arquivo}'!")

except Exception as e:
    print(f"❌ Ocorreu um erro ao gerar o gráfico: {e}")