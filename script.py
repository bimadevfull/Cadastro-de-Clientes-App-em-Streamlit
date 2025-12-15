# script simples: pede nome e idade, verifica maioridade e salva uma linha no CSV

nome = input("Digite o seu nome: ")
try:
    idade = int(input("Digite a sua idade: "))
except ValueError:
    print("Idade inválida. Use apenas números.")
else:
    print(nome)

    if idade > 17:
        print("Você pode entrar na festa!")

    # salva no arquivo (modo append)
    with open("base_dados.csv", "a", encoding="utf-8", newline="") as arquivo:
        arquivo.write(f"Seja bem vindo(a) {nome}.\n")