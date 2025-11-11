import sympy

# 1. Defina 'x' como um símbolo
x = sympy.symbols('x')

# --- Defina sua função e o ponto 'a' aqui ---

# Exemplo 1: lim x->2 (x^2)
f = (x**2 - 12) / (x - 2)
a = 2

# Exemplo 2: lim x->0 (sin(x) / x)
# f = sympy.sin(x) / x
# a = 0

# Exemplo 3: lim x->1 ( (x^2 - 1) / (x - 1) )
# f = (x**2 - 1) / (x - 1)
# a = 1

# -----------------------------------------------

# 3. Calcule o limite
try:
    L = sympy.limit(f, x, a)

    print(f"Função f(x): {f}")
    print(f"Valor de a: {a}")
    print(f"O limite de f(x) quando x -> {a} é: {L}")

except Exception as e:
    print(f"Não foi possível calcular o limite: {e}")