import plotly.express as px
import pandas as pd

# --- 1. Dependências ---
# Lembre-se de que você precisa do 'kaleido' instalado para salvar a imagem:
# pip install kaleido

# --- 2. Função Auxiliar ---
# (Necessária para gerar o intervalo decimal para 'x')
def frange(start, stop, step):
    """Gera um range que aceita passos decimais."""
    while start <= stop:
        yield start
        start += step

# --- 3. Definição das Entradas ---
#
# Altere os valores aqui para definir sua função e o intervalo
#
a = 1
b = -5
c = 6
x_min = -10.0
x_max = 10.0
passo = 0.1 # Densidade dos pontos no gráfico

nome_arquivo = "parábola.png" # Nome do arquivo de saída

# --- 4. Lógica Principal (Cálculo e Plotagem) ---

try:
    # Calcular os pontos da parábola
    x_vals = [round(i, 2) for i in frange(x_min, x_max, passo)]
    y_vals = [a * (xi ** 2) + b * xi + c for xi in x_vals]
    
    # Criar o DataFrame para o Plotly
    df = pd.DataFrame({"x": x_vals, "y": y_vals})

    # Criar o gráfico
    titulo = f"y = {a}x² + {b}x + {c}"
    fig = px.line(df, x="x", y="y", title=titulo, markers=False) 

    # --- 5. Estilização (Opcional) ---
    fig.update_traces(line=dict(color="royalblue", width=2))
    fig.update_layout(
        plot_bgcolor="#f7f7f7",      # Cor de fundo do gráfico
        xaxis_title="Eixo X",
        yaxis_title="Eixo Y",
        hovermode="x unified",       # Tooltip unificado
        title_font=dict(size=14, family="Arial", color="black")
    )

    # Adicionar linhas dos eixos x=0 e y=0
    fig.add_hline(y=0, line_width=1, line_color="black")
    fig.add_vline(x=0, line_width=1, line_color="black")

    # --- 6. Salvar o Gráfico ---
    fig.write_image(nome_arquivo)

    print(f"✅ Gráfico gerado e salvo com sucesso como '{nome_arquivo}'!")

except Exception as e:
    print(f"❌ Ocorreu um erro ao gerar o gráfico: {e}")