import sympy
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Defina as Entradas Aqui ---

# Define 'x' como um símbolo
x = sympy.symbols('x')

# f = x**2
f = sympy.sin(x) + 1  # Exemplo 2: uma senoide
# f = 4 - x**2            # Exemplo 3: parábola invertida

# Limites de integração
a = 0
b = 5

# Número de pontos para o gráfico (suavidade)
n = 200

nome_arquivo = "area_plot.png"

# --------------------------------------

try:
    # --- 2. Cálculo Simbólico da Área (Integral) ---
    area = sympy.integrate(f, (x, a, b))
    
    # Avalia a área para um valor numérico decimal
    area_num = area.evalf()

    print(f"Função f(x): {f}")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Área Exata (Integral): {area}")
    print(f"Valor Numérico da Área: {area_num:.6f}")

    # --- 3. Preparação para o Gráfico ---
    
    # Converte a função simbólica 'f' em uma função numérica rápida
    # que o numpy/matplotlib podem usar
    f_num = sympy.lambdify(x, f, 'numpy')

    # Cria 'n' valores de x linearmente espaçados entre 'a' e 'b'
    x_vals = np.linspace(a, b, n)
    
    # Calcula os valores de y correspondentes
    y_vals = f_num(x_vals)

    # --- 4. Geração do Gráfico com Matplotlib ---
    
    plt.figure(figsize=(9, 6)) # Define o tamanho da imagem

    # Plota a linha da função
    plt.plot(x_vals, y_vals, color='blue', label=f'f(x) = {f}', linewidth=2)

    # Preenche (hachura) a área entre a curva (y_vals) e o eixo x (y=0)
    plt.fill_between(
        x_vals,    # Pontos x
        y_vals,    # Limite superior (a curva)
        0,         # Limite inferior (o eixo x)
        color='lightblue', 
        alpha=0.6, # Transparência
        label=f'Área = {area_num:.4f}'
    )

    # --- 5. Estilização do Gráfico ---
    
    # Adiciona linhas de eixo (x=0 e y=0)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.title('Visualização da Área sob a Curva')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend() # Mostra as legendas
    plt.grid(True, linestyle='--', alpha=0.5) # Grade pontilhada
    
    # Salva a imagem
    plt.savefig(nome_arquivo)
    
    print(f"\nGráfico salvo com sucesso como '{nome_arquivo}'!")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")