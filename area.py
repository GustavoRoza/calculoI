import sympy
import numpy as np
import matplotlib.pyplot as plt

x = sympy.symbols('x')

f = x**2
#f = sympy.sin(x) + 1  
#f = 4 - x**2            

# Limites de integração
a = -2
b = 2

n = 200 #pontos para o gráfico

nome_arquivo = "area_plot.png"

# --------------------------------------

try:

    area = sympy.integrate(sympy.Abs(f), (x, a, b)) # Abs() torna tudo positivo
    area_num = area.evalf()

    print(f"Função f(x): {f}")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Área Exata (Integral): {area}")
    print(f"Valor Numérico da Área: {area_num:.6f}")

    f_num = sympy.lambdify(x, f, 'numpy')

    x_vals = np.linspace(a, b, n)
    y_vals = f_num(x_vals)
    
    plt.figure(figsize=(9, 6)) 
    plt.plot(x_vals, y_vals, color='blue', label=f'f(x) = {f}', linewidth=2)

    plt.fill_between(
        x_vals,    
        y_vals,    
        0,         
        color='lightblue', 
        alpha=0.6, 
        label=f'Área = {area_num:.4f}'
    )
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.title('Visualização da Área sob a Curva')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5) # Grade pontilhada

    plt.savefig(nome_arquivo)
    
    print(f"\nGráfico salvo com sucesso como '{nome_arquivo}'!")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")