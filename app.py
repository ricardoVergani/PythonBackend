import os


restaurantes = [{"nome": "Viena", "categoria": "Geral", "ativo": False}, 
                {"nome": "America", "categoria": "Geral", "ativo": True},
                {"nome": "Natory", "categoria": "Sushi", "ativo": False},
                ]


def nome():
    print( """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def voltar():
    print("\nDigite uma tecla para voltar ao menu ")
    main()


def exibir_sub(texto):
    os.system('cls')
    print(texto)
    print()

def menu():
    print("1- Cadastrar Restaurante")
    print("2- Listar Restaurante")
    print("3- Ativar Restaurante")
    print("4- Sair\n")

def finalizando():
    exibir_sub("Finalizando...")


def invalido():
    print("Opcao invalida")
    voltar()


def alternar():
    exibir_sub("Alternando estado...")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar: ")
    restaurante_encontrado = False


    for restaurante in restaurantes:
        if nome_restaurante == restaurante[nome]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem =  f" O resturante {restaurante} foi ativado com sucesso " if restaurante["ativo"] else f" O resturante {restaurante} foi desativado com sucesso "
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante nao foi encontrado")



    voltar()

def cadastrar():
    exibir_sub("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do retaurante que deseja cadastrar")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}")
    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"Cadastro do restaurante{nome_restaurante} foi cadastrado com sucesso")
    voltar()



def listar():
    exibir_sub("Listando Restaurantes")

    print (f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")

    for restaurante in restaurantes:
        nome_restaurante =  restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} " ) 

    voltar()



def escolha():


    try:
        opcao_escolhida = int(input("Escolha a opcao a ser realizada: "))

        if opcao_escolhida == 1 :
            cadastrar()
        elif opcao_escolhida == 2:
            listar()
        elif opcao_escolhida == 3:
            alternar()
        elif opcao_escolhida == 4:
            finalizando()
        else:
            invalido()
    except:
        invalido()
    
def main():
    os.system("cls")
    nome()
    menu()
    escolha()


if __name__ == "__main__":
    main()


