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
    
    #andares atuais dos elevadores principais
    elevador_c = -2
    elevador_b = -1
    elevador_a = 0
    elevador_d = 301
    elevador_e = 301
    elevador_f = 303
    
    #andares atuais dos elevadores secundarios
    elevador_g = -2
    elevador_h = -1
    elevador_i = 0
    elevador_j = 301
    elevador_k = 301
    elevador_l = 303
    
    #contadores de energia e tempo de espera
    cont_energ_a = 0
    cont_energ_b = 0
    cont_energ_c = 0
    cont_t_a = 0
    cont_t_b = 0
    cont_t_c = 0
    
    contador = 0
    contador2 = 0
    
    #primeira entrada
    requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
    if requisicoes[0] != []:
        while requisicoes != ([], []):
            if requisition() == True:
                requisicoes = None
                requisicoes = organiza_req(requisicoes_tunel1, requisicoes_tunel3)
            
            #subindo
            os.system("cls")
            if elevador_b < 0:
                #somente elevador a
                print("Elevador A atendendo as requisicoes!")
                for auxiliar in requisicoes[0]:
                    if auxiliar[0] == elevador_a and teste[0] != teste[1]:
                        print("Porta aberta(elevador A)!")
                
                if requisicoes[0] != []:
                    #elevador a, b e c
                    contador = 0
                    for teste in requisicoes[0]:
                        if teste[0] == elevador_a - 1:
                            requisicoes[0][contador] = (requisicoes[0][contador][0] + 1, requisicoes[0][contador][1])
                        contador = contador + 1    
                        
                    for teste in requisicoes[0]:
                        if teste[0] == teste[1]:
                            print("Porta aberta(elevador A)!")
                            requisicoes[0].pop()
            else:
                #elevador a e b
                if elevador_c > -1:
                    print("Elevador A, elevador B e elevador C atendendo as requisicoes!")
                else:
                    print("Elevador a e elevador B atendendo as requisicoes!")
                    for auxiliar in requisicoes[0]:
                        if auxiliar[0] == elevador_a and auxiliar[0] != auxiliar[1]:
                            print("Porta aberta(elevador A)!")
                        if auxiliar[0] == elevador_b and auxiliar[0] != auxiliar[1]:
                            print("Porta aberta(elevador B)!")
                    
                    if requisicoes[0] != []:
                        contador = 0
                        for teste in requisicoes[0]:
                            if teste[0] == elevador_a - 1:
                                requisicoes[0][contador] = (requisicoes[0][contador][0] + 1, requisicoes[0][contador][1])
                            if teste[0] == elevador_b - 1:
                                requisicoes[0][contador] = (requisicoes[0][contador][0] + 1, requisicoes[0][contador][1])
                            contador = contador + 1
                            
                        for teste in requisicoes[0]:
                            if teste[0] == teste[1]:
                                requisicoes[0].pop()
                                if elevador_a == teste[0]:
                                    print("Porta aberta(elevador A)!")
                                    elevador_a = 0
                                if elevador_b == teste[0]:
                                    print("Porta aberta(elevador B)!")
                                    elevador_c = -1
                                if elevador_c == teste[0]:
                                    print("Porta aberta(elevador C)!")
                                    elevador_c = - 2
            
            
            #print(f"{requisicoes}\n")
            
            contador2 = 0
            for assistant in requisicoes[0]:
                #print(f"Gasto energetico de A: {cont_energ_a}\nTempo de A: {cont_t_a}\nAndar atual do elevador A: {elevador_a}")
                if assistant[0] < elevador_a:
                    if elevador_b <= assistant[0]:
                        print(f"Gasto energetico de A: {cont_energ_a}\nTempo de A: {cont_t_a}\nAndar atual do elevador A: {elevador_a}")
                        print(f"Gasto energetico de B: {cont_energ_b}\nTempo de B: {cont_t_b}\nAndar atual do elevador B: {elevador_b}")
                        elevador_a = elevador_a + 1
                        cont_energ_a = cont_energ_a + 1
                        contador2 = contador2 + 1
                        cont_t_a = cont_t_a + 1
                        
                        elevador_b = elevador_b + 1
                        cont_energ_b = cont_energ_b + 1
                        cont_t_b = cont_t_b + 1
                    else:
                        print(f"Gasto energetico de A: {cont_energ_a}\nTempo de A: {cont_t_a}\nAndar atual do elevador A: {elevador_a}")
                        print(f"Gasto energetico de B: {cont_energ_b}\nTempo de B: {cont_t_b}\nAndar atual do elevador B: {elevador_b}")
                        print(f"Gasto energetico de C: {cont_energ_c}\nTempo de C: {cont_t_c}\nAndar atual do elevador C: {elevador_c}")
                        elevador_a = elevador_a + 1
                        cont_energ_a = cont_energ_a + 1
                        contador2 = contador2 + 1
                        cont_t_a = cont_t_a + 1
                        
                        elevador_b = elevador_b + 1
                        cont_energ_b = cont_energ_b + 1
                        cont_t_b = cont_t_b + 1
                        
                        elevador_c = elevador_c + 1
                        cont_energ_c = cont_energ_c + 1
                        cont_t_c = cont_t_c + 1
                else:
                    if contador2 == len(requisicoes[0]) - 1:
                        print(f"Gasto energetico de A: {cont_energ_a}\nTempo de A: {cont_t_a}\nAndar atual do elevador A: {elevador_a}")
                        elevador_a = elevador_a + 1
                        cont_energ_a = cont_energ_a + 1
                        contador2 = contador2 + 1
                        cont_t_a = cont_t_a + 1
                contador2 = contador2 + 1
            
            if requisicoes[0] == []:
                print("Requisicoes atendidas!")
                break
    
    elevador_a = 0

main()
