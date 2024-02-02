itens_quantity = int(input("Quantos itens você deseja comprar? "))


itens_list = []

for item in range(itens_quantity):
    while True:
        itens_wanted = input(f"item {item+1}: ")
        if itens_wanted.isdigit():
            print("Numeros nao sao permitidos")
            continue
        else: break

    itens_list.append(itens_wanted)



def enumerate_lista(list):
    print("Assim ficou sua lista...")

    for number, item in enumerate(list, 1):
        print(F"{number} - {item}")



while True:
    enumerate_lista(itens_list)
    question1 = input('Deseja adicionar/remover algum item? Caso não queira, insira "Não" ').lower()
    
    if "n" in question1: break



    if question1 == 'remover':
        item_remover = input("Que item você deseja remover? insira nome/número: ")
            
        if item_remover.isdigit():
            index_remover = int(item_remover) - 1
            try:
                itens_list.pop(index_remover)
            except:
                print("Número não está presente na lista, verifique se está certo!")
                continue


        elif item_remover in itens_list:
            try:
                itens_list.remove(item_remover)
            except:
                print("O item não está presente na lista, verifique se está certo!")
                continue



    elif question1 == 'adicionar':
        item_adder = input("Que item você deseja adicionar? ")

        if item_adder.isdigit():
            print("Não é permitido adicionar números")
            continue

        itens_list.append(item_adder)



    else:
        print('Digite apenas "adicionar/remover"')
        continue