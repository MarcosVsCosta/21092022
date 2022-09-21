texto = input("Digite uma palavra ou frase - ")

tamanho = len(texto)-1 
invertido = []

while tamanho >= 0:
    invertido.append(texto[tamanho])
    tamanho = tamanho -1

print ("".join(invertido))