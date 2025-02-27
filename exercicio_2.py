# 2) Fibonacci e verificação se pertence à sequência
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if fibonacci(numero):
    print(f"2) O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"2) O número {numero} não pertence à sequência de Fibonacci.")