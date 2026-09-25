import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar_tela()
    
    escolha = input("quer ver pares ou impares? ")
    numero = int(input("qual o numero limite? "))
    
    contador = 1
    
    while contador <= numero:
        # Verifica se deve mostrar
        e_par = (contador % 2 == 0)
        e_impar = (contador % 2 == 1)
        
        if escolha.lower() == "pares" and e_par:
            print(contador)
        elif escolha.lower() == "impares" and e_impar:
            print(contador)
        
        contador = contador + 1  # ✅ SEMPRE avança, fora do if!
    
    continuar = input("\nver outra contagem? (s/n): ")
    if continuar.lower() == "n":
        print("Obrigado por usar o programa!")
        break