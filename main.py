import os


def entrada():
    floor_current = int(input("Digite seu andar atual: "))
    #os.system("cls")    
    floor_destiny = int(input("Digite seu andar de destino: "))
    #os.system("cls")
    
    if floor_current < 1 or floor_destiny > 300:
        print("voce digitou um andar invalido!")
        organiza_req()
    return (floor_current, floor_destiny)

    
def up(floor_current, floor_destiny):
    if floor_current > floor_destiny:
        return False
    else:
        return True


def requisition():
    requisit = int(input("Ha alguma requisicao?\n\t1 - Sim\n\t2 - Nao\n\t\tOpcao: "))
    if requisit == 1:
        return True
    elif requisit == 2:
        return False
    else:
        print("Entrada invalida!")
        requisition()

def organiza_req(requisicoes_tunel1, requisicoes_tunel3):
    #entrada de dados
    dados = entrada()
    floor_current = dados[0]
    floor_destiny = dados[1]
    if up(floor_current, floor_destiny) == True:
        requisicoes_tunel1.append(dados)
    else:
        requisicoes_tunel3.append(dados)
    
    auxiliar = 0
    auxiliar2 = None
    auxiliar3 = 0
    auxiliar4 = None
    if requisicoes_tunel1 != [] and len(requisicoes_tunel1) > 1:
        #insert sort
        while auxiliar < len(requisicoes_tunel1) - 1:
            if requisicoes_tunel1[auxiliar][1] < requisicoes_tunel1[auxiliar + 1][1]:
                auxiliar2 = requisicoes_tunel1[auxiliar]
                requisicoes_tunel1[auxiliar] = requisicoes_tunel1[auxiliar + 1]
                requisicoes_tunel1[auxiliar + 1] = auxiliar2
                if auxiliar > 0:
                    auxiliar3 = auxiliar
                    while auxiliar3 > 0:
                        if requisicoes_tunel1[auxiliar3][1] > requisicoes_tunel1[auxiliar3 - 1][1]:
                            auxiliar4 = requisicoes_tunel1[auxiliar3]
                            requisicoes_tunel1[auxiliar3] = requisicoes_tunel1[auxiliar3 - 1]
                            requisicoes_tunel1[auxiliar3 - 1] = auxiliar4
                        auxiliar3 = auxiliar3 - 1
            auxiliar = auxiliar + 1
            
    auxiliar = 0
    auxiliar2 = None
    auxiliar3 = 0
    auxiliar4 = None
    if requisicoes_tunel3 != [] and len(requisicoes_tunel3) > 1:
        #insert sort
        while auxiliar > len(requisicoes_tunel3) - 1:
            if requisicoes_tunel3[auxiliar][1] > requisicoes_tunel3[auxiliar + 1][1]:
                auxiliar2 = requisicoes_tunel3[auxiliar]
                requisicoes_tunel3[auxiliar] = requisicoes_tunel3[auxiliar + 1]
                requisicoes_tunel3[auxiliar + 1] = auxiliar2
                if auxiliar > 0:
                    auxiliar3 = auxiliar
                    while auxiliar3 > 0:
                        if requisicoes_tunel3[auxiliar3][1] < requisicoes_tunel3[auxiliar3 - 1][1]:
                            auxiliar4 = requisicoes_tunel3[auxiliar3]
                            requisicoes_tunel3[auxiliar3] = requisicoes_tunel3[auxiliar3 - 1]
                            requisicoes_tunel3[auxiliar3 - 1] = auxiliar4
                        auxiliar3 = auxiliar3 - 1
            auxiliar = auxiliar + 1
    
    return (requisicoes_tunel1, requisicoes_tunel3) 

def logica():
    pass

def main():
    print("\n===================================\nBem vindo ao sistema de elevadores!\n===================================\n")
    
    #tuneis subindo
    requisicoes_tunel1 = []
    #tuneis descendo
    requisicoes_tunel3 = []
    
    #andares atuais do elevador
    elevador_c = -2
    elevador_b = -1
    elevador_a = 0
    elevador_d = 301
    elevador_e = 301
    elevador_f = 303
    
    #contadores de energia e tempo de espera
    cont_energ_a = 0
    cont_energ_d = 0
    cont_t_a = 0
    cont_t_d = 0
    
    contador = 0
    contador2 = 0
    
    #primeira entrada
    requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
    while requisicoes != None:
        if requisition() == True:
            requisicoes = None
            requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
        if requisicoes[0] != []:
            contador = 0
            os.system("cls")
            for teste in requisicoes[0]:
                if teste[0] == elevador_a - 1:
                    requisicoes[0][contador] = (requisicoes[0][contador][0] + 1, requisicoes[0][contador][1])
                contador = contador + 1
            
            for teste in requisicoes[0]:
                if teste[0] == teste[1]:
                    print("Porta aberta!")
                    requisicoes[0].pop()
        
        if requisicoes[1] != []:
            contador = 0
            os.system("cls")
            for teste in requisicoes[1]:
                if teste[0] == elevador_d + 1:
                    requisicoes[1][contador] = (requisicoes[1][contador][0] - 1, requisicoes[0][contador][1])
                contador = contador + 1
            
            for teste in requisicoes[1]:
                if teste[0] == teste[1]:
                    print("Porta aberta!")
                    requisicoes[0].pop()
         
        elevador_a = elevador_a + 1   
        elevador_d = elevador_d - 1
        cont_energ_a = cont_energ_a + 1
        cont_energ_d = cont_energ_d + 1
        cont_t_a = cont_t_a + 1
        cont_t_d = cont_t_d + 1
        print(f"Gasto energetico de A: {cont_energ_a}\nGasto energetico D: {cont_energ_d}\nTempo de A: {cont_t_a}\nTempo de D: {cont_t_d}\nAndar atual do elevador A: {elevador_a}\nAndar atual do elevador D: {elevador_d}\nGasto total de energia: {cont_energ_a + cont_energ_d}")
        contador2 = contador2 + 1
        
        print(requisicoes)
            
        if requisicoes == ([], []):
            print("Requisicoes atendidas!")
            break
    elevador_a = 0

main()
