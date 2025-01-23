Inventory = []
check = True

# Função para Adicionar Item
# Para 'adicionar', retorne uma mensagem como: 'Item adicionado com sucesso.'
def add_item():
    item = input("Insira o Nome do Item que Deseja Adicionar ao Inventário: ")
    Inventory.append(item)
    print(f"O Item {item} foi Adicionado com sucesso\n")
    return Inventory

# Função para Remover Item
# Para 'remover', retorne: 'Item removido com sucesso.' ou uma mensagem de erro se o item não estiver presente.
def rem_item():
    rem = input("Insira o Nome do Item que Deseja Remover do Inventário: ")
    if rem in Inventory:
        Inventory.remove(rem)
        print(f"O Item {rem} foi removido com sucesso\n")
    else:
        print("Item não encontrado!\n")
    return Inventory

# Função para Listar o Inventário
# Para 'listar', retorne todos os itens no inventário, ou uma mensagem como: 'Inventário vazio.'
def list_ivent():
    if len(Inventory) > 0:
        print(Inventory)
    else:
        print("Inventário vazio!")
    return Inventory

while check == True:
    print("Seja Bem Vindo ao seu Inventário maior Mago de FrozenWest!")
    print('''Insira a opção desejada:
    1 - Adicionar Item ao Inventário
    2 - Remover Item do Inventário
    3 - Listar Inventário
    4 - Sair
''')
    
    choice = int(input(">>"))

    if choice == 1:
        add_item()
    elif choice == 2:
        rem_item()
    elif choice == 3:
        list_ivent()
    elif choice == 4:
        print("Saindo do Inventário... Até a próxima!")
        check = False
    else:
        print("Valor inválido! Tente novamente.")