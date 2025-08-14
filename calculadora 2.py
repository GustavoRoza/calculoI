import plotly.express as px
import pandas as pd

def gerar_grafico(a: float, b: float, c: float, x_min: int, x_max: int):
    """Gera e exibe o gráfico interativo de uma equação do 2º grau."""
    x = list(range(x_min, x_max + 1))
    y = [a * (xi ** 2) + b * xi + c for xi in x]

    # Criar DataFrame para o Plotly
    df = pd.DataFrame({"x": x, "y": y})

    # Criar gráfico interativo
    fig = px.line(
        df, x="x", y="y",
        title=f"y = {a}x² + {b}x + {c}",
        markers=True
    )

    # Personalizar layout
    fig.update_traces(line=dict(color="royalblue", width=3),
                      marker=dict(size=8, color="orange"))
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        title_x=0.5
    )

    # Exibir
    fig.show()
    fig.write_image("grafico.png")  # Salva no mesmo diretório


def main():
    print("=== Calculadora de Equação do 2º Grau ===")
    print("Formato: y = ax² + bx + c (Exemplo: 1 -4 3)\n")

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    x_min = int(input("Digite o valor de x mínimo: "))
    x_max = int(input("Digite o valor de x máximo: "))

    gerar_grafico(a, b, c, x_min, x_max)


if __name__ == "__main__":
    main()
