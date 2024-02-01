itens_quantity = int(input("Quantos itens voce deseja comprar? "))


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
    question1 = input('Deseja adicionar/remover algum item? Caso não queira, insira "Nao" ').lower()
    
    if "nao" in question1: break
        


    if question1 == 'remover':
        iten_remover = input("Que item voce deseja remover? insira nome/numero: ")
            
        if iten_remover.isdigit():
            index_remover = int(iten_remover) - 1
            try:
                itens_list.pop(index_remover)
            except:
                print("Numero nao esta presente na lista, verifique se esta certo!")
                continue


        elif iten_remover in itens_list:
            try:
                itens_list.remove(iten_remover)
            except:
                print("O item nao esta presente na lista, verifique se esta certo!")
                continue
        


    elif question1 == 'adicionar':
        iten_adder = input("Que item voce deseja adicionar? ")

        if iten_adder.isdigit():
            print("Não é permitido adicionar numeros")
            break

        itens_list.append(iten_adder)
            
    

    else:
        print('Digite apenas "adicionar/remover"')
        continue