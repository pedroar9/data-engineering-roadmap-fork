CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salario: "))


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus Por exemplo(2.0): "))


# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario


# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bônus
print(f"O usuario {nome_usuario} possui o bônus de {valor_do_bonus}")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# 1) O programa não valida se o usuário digitou um número válido para o salário
# 2) O programa não valida se o usuário digitou um número válido para o bônus
# 3) O programa não valida se o usuário digitou um nome válido
# 4) O programa não valida se o usuário digitou um bônus válido     
# 5) O programa não valida se o usuário digitou um salário válido
# 6) O programa não valida se o usuário digitou um nome válido              
# 7) O programa não valida se o usuário digitou um bônus válido
# 8) O programa não valida se o usuário digitou um salário válido
# 9) O programa não valida se o usuário digitou um nome válido
# 10) valores negativos para salário e bônus
# 11) Bônus com valor inteiro