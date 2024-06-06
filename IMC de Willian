def calculadora_imc():
    # Solicita o peso do usuário
    peso = float(input("Digite o seu peso (em kg): "))
    
    # Solicita a altura do usuário
    altura = float(input("Digite a sua altura (em metros): "))
    
    # Calcula o IMC
    imc = peso / (altura ** 2)
    
    # Exibe o IMC calculado
    print(f"Seu IMC é: {imc:.2f}")
    
    # Classifica o IMC
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 25.0:
        print("Classificação: Peso adequado")
    elif 25.0 <= imc < 30.0:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obeso")

# Executa a função
calculadora_imc()
