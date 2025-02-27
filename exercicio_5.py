# 5) Inversão de string sem função pronta
def inverte_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

texto = input("Informe uma palavra ou frase para inverter: ")
print(f"5) String invertida: {inverte_string(texto)}")