import sympy

x = sympy.symbols('x')

f = (x**2 - 4) / (x - 2)
a = 2
# ----------------------

print(f"--- Resolvendo por aproximação numérica usando a definição ---")
print(f"Analisando f(x) = {f} quando x -> {a}\n")
print(f"{'distancia do X ao a':<22} | {'X tendendo pela esquerda (a-h)':<35} | {'X tendendo pela direita (a+h)':<35}")
print("-" * 100) # Aumentei a linha divisória também

h = 0.1
try:
    for i in range(5):
        val_esq = f.subs(x, a - h).evalf()
        val_dir = f.subs(x, a + h).evalf()
        print(f"{h:<22.6f} | {val_esq:<35.4f} | {val_dir:<35.4f}")
        h /= 10
except Exception as e:
    print(f"Erro na aproximação: {e}")

print("\n" + "-" * 65)


try:
    L = sympy.limit(f, x, a) 
    print(f"--- Resultado Exato ---")
    print(f"Limite calculado: {L}")
    
    if L.is_infinite or L == sympy.nan:
        L_dir = sympy.limit(f, x, a, '+')
        L_esq = sympy.limit(f, x, a, '-')
        print(f"Lateral Direita: {L_dir}")
        print(f"Lateral Esquerda: {L_esq}")

except Exception as e:
    print(f"Não foi possível calcular o limite exato: {e}")