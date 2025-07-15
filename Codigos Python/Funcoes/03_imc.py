def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    Args:
    peso (float): O peso da pessoa em quilogramas.
    altura (float): A altura da pessoa em metros.

    Returns:
    float: O valor do IMC arredondado para duas casas decimais.
    """
    return round(peso / (altura ** 2), 2)

def categoria_imc(imc):
    """
    Determina a categoria de IMC com base no valor calculado.
    
    Args:
    imc (float): O valor do IMC.

    Returns:
    str: A categoria correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Programa principal
def main():
    print("Calculadora de IMC")
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros): "))
        
        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        # Determina a categoria
        categoria = categoria_imc(imc)
        
        print(f"\nSeu IMC é: {imc}")
        print(f"Categoria: {categoria}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para peso e altura.")

# Executa o programa
if __name__ == "__main__":
    main()
