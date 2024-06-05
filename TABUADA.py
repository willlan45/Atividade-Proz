
tabuada = int(input("Digite um número para a tabuada: "))

for count in range(10):
    resultado = tabuada * (count + 1)
    print(f"{tabuada} x {count + 1} = {resultado}")
