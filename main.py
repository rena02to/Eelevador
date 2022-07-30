import os


def entrada():
    floor_current = int(input("Digite seu andar atual: "))
    os.system("cls")    
    floor_destiny = int(input("Digite seu andar de destino: "))
    os.system("cls")
    
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
                auxiliar2 = requisicoes_tunel1[auxiliar][1]
                requisicoes_tunel1[auxiliar] = requisicoes_tunel1[auxiliar + 1][1]
                requisicoes_tunel1[auxiliar + 1][1] = auxiliar2
                if auxiliar > 0:
                    auxiliar3 = auxiliar
                    while auxiliar3 > 0:
                        if requisicoes_tunel1[auxiliar3][1] > requisicoes_tunel1[auxiliar3 - 1][1]:
                            auxiliar4 = requisicoes_tunel1[auxiliar3][1]
                            requisicoes_tunel1[auxiliar3][1] = requisicoes_tunel1[auxiliar3 - 1][1]
                            requisicoes_tunel1[auxiliar3 - 1][1] = auxiliar4
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
                auxiliar2 = requisicoes_tunel3[auxiliar][1]
                requisicoes_tunel3[auxiliar] = requisicoes_tunel3[auxiliar + 1][1]
                requisicoes_tunel3[auxiliar + 1][1] = auxiliar2
                if auxiliar > 0:
                    auxiliar3 = auxiliar
                    while auxiliar3 > 0:
                        if requisicoes_tunel3[auxiliar3][1] < requisicoes_tunel3[auxiliar3 - 1][1]:
                            auxiliar4 = requisicoes_tunel3[auxiliar3][1]
                            requisicoes_tunel3[auxiliar3][1] = requisicoes_tunel3[auxiliar3 - 1][1]
                            requisicoes_tunel3[auxiliar3 - 1][1] = auxiliar4
                        auxiliar3 = auxiliar3 - 1
            auxiliar = auxiliar + 1
    
    return (requisicoes_tunel1, requisicoes_tunel3)
    

def main():
    print("\n===================================\nBem vindo ao sistema de elevadores!\n===================================\n")
    
    #tuneis subindo
    requisicoes_tunel1 = []
    #tuneis descendo
    requisicoes_tunel3 = []
    
    #primeira entrada
    requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
    while requisicoes != None:
        if requisition() == True:
            requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
        print(requisicoes)
    
    #andares atuais do elevador
    elevador_a = -2
    elevador_b = -1
    elevador_c = 0

    #contadores de energia e tempo de espera
    cont_energ = None
    cont_t = None
    
    #atende as requisicoes
    #while requisicoes_tunel1 != [] and requisicoes_tunel2 != [] and requisicoes_tunel3 != [] and requisicoes_tunel4 != []:
        
    

main()
