# Atividade #
#LAB - Música Viva Mariana
#Resolver em três níveis

#1-for simples;
#2-for com diferenciação de singular e plural;
#3-estrutura completa com a complexidade do texto "é n", "é n+1".
# -------------------------------------- #
# Loop para contar de 1 até 10
for i in range(1, 11):
    # Exibe a contagem de Mariana
    print(f"Mariana conta {i}")
    # Imprime a parte inicial antes de listar os números
    print(f"Mariana conta {i}: ", end="")
    # Loop para contar até o número atual de 'i'
    for j in range(1, i + 1):
        # Se for o último número da sequência, imprime com vírgula
        if j == i:
            print(f"é {j}, ", end="")
        else:
            # Imprime os números seguidos de vírgula
            print(f"é {j}, ", end="")   
    # Se a contagem chegar a 3, imprime "é!"
    if i == 3:
        print("é!")
    else:
        # Caso contrário, imprime "é Ana"
        print("é Ana")
    # Imprime uma mensagem no final de cada ciclo de contagem
    print("Viva a Mariana, viva a Mariana\n")
