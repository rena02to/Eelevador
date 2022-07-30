from operator import pos
import os
import math
from tarfile import PAX_FIELDS
from turtle import position


def elevator(floor_current, y):
    x = floor_current / 25
    x = x - ((y - 1) * 3)
    return math.ceil(x)


def up_down(floor_current, floor_destiny):
    if floor_current < floor_destiny:
        return 1
    else:
        return -1


def tunnel(floor_current):
    if floor_current <= 75:
        return 1
    elif floor_current <= 150:
        return 2
    elif floor_current <= 225:
        return 3
    elif floor_current <= 300:
        return 4


def main():
    floor_current = int(input("Por gentileza, digite seu andar atual.\n\tAndar:"))
    if floor_current > 300 or floor_current < 1:
        while floor_current > 300 or floor_current < 1:
            os.system("cls")
            print("=========================\n\tAndar invalido!\n=========================")
            floor_current = int(input("Por gentileza, digite seu andar atual.\n\tAndar:"))
    
    os.system("cls")
    floor_destiny = int(input("Por gentileza, digite seu andar de destino.\n\tAndar:"))
    if floor_destiny > 300 or floor_destiny < 1:
        while floor_destiny < 1 or floor_destiny > 300:
            os.system("cls")
            print("=========================\n\tAndar invalido!\n=========================")
            floor_destiny = int(input("Por gentileza, digite seu andar de destino.\n\tAndar:"))
    
    if floor_destiny == floor_current:
        os.system("cls")
        print("Os andares de partida e de destino sao iguais.\nTe direcionando para a tela inicial...")
        floor_current = int(input("Por gentileza, digite seu andar atual.\n\tAndar:"))
        if floor_current > 300 or floor_current < 1:
            while floor_current > 300 or floor_current < 1:
                os.system("cls")
                print("=========================\n\tAndar invalido!\n=========================")
                floor_current = int(input("Por gentileza, digite seu andar atual.\n\tAndar:"))
        
        os.system("cls")
        floor_destiny = int(input("Por gentileza, digite seu andar de destino.\n\tAndar:"))
        if floor_destiny > 300 or floor_destiny < 1:
            while floor_destiny < 1 or floor_destiny > 300:
                os.system("cls")
                print("=========================\n\tAndar invalido!\n=========================")
                floor_destiny = int(input("Por gentileza, digite seu andar de destino.\n\tAndar:"))
    
    os.system("cls")
    print("==============================\nRESPONDA ESSA TELA COM ATENCAO\n==============================")
    correct = None
    while correct != 1 or correct != 2:
        correct = int(input(f"Os dados foram inseridos corretamente?\nAndar de partida: {floor_current}\nAndar de destino: {floor_destiny}\n   [1] - Sim\n   [2] - Nao\n      Opcao: "))
        if correct == 2:
            os.system("cls")
            print("Iremos te encaminhar para a tela inicial...")
            main()
        elif correct == 1:
            os.system("cls")
            print("Processando sua requisicao.\nAguarde...")
            break
        else:
            os.system("cls")
            print("=========================\n\tOpcao invalida!\n=========================")
        
    if floor_current > floor_destiny:
        amount = math.ceil((floor_current - floor_destiny) / 75)
    else:
        amount = math.ceil((floor_destiny - floor_current) / 75)
    
    os.system("cls")
    
    
    print("\tPara fins de informar ao usuario, quando um elevador chega ao andar, e outro precisa usar aquele espaco, o que esta no andar, desce/sobe para um andar posterior/superior.")
    print(f"\tInformamos que sera(o) necessario(s) {amount} tunel(ies) para te levar ate seu destino.\n\n")
    
    tunel = tunnel(floor_current)
    elevador = elevator(floor_current, tunel) - 1
    proxima_posicao = None
    tunel = tunel - 1
    if up_down(floor_current, floor_destiny) == 1:
        position = [[1, 25, 50], [75, 100, 125], [150, 175, 200], [225, 250, 275]]
        if floor_current > 275:
            elevador = 2
            tunel = 3
            print(f"Andar atual: {floor_current}")
            print(f"O elevador {elevador + 1} do tunel {tunel + 1} ira te levar ao seu destino!")
            floor_current = floor_destiny
            
        if floor_current != floor_destiny:
            if elevador == 2:
                if position[tunel + 1][0] == floor_current:
                    tunel = tunel + 1
                    elevador = 0
            elif position[tunel][elevador + 1] == floor_current:
                elevador = elevador + 1
                
        while floor_current != floor_destiny:
            print("----------------------------------------------------------------------------------------------------")
            if elevador == 2:
                if tunel < 3:
                    proxima_posicao = position[tunel + 1][0]
                else:
                    proxima_posicao = 300
            else:
                proxima_posicao = position[tunel][elevador + 1]
            
            if proxima_posicao >= floor_destiny:
                print(f"Andar atual: {floor_current}")
                if elevador >= 3:
                    print(f"O elevador {1} do tunel {tunel + 2} ira te levar ao seu destino!")
                else:
                    print(f"O elevador {elevador + 1} do tunel {tunel + 1} ira te levar ao seu destino!")
                floor_current = floor_destiny
            else:
                print(f"Andar atual: {floor_current}")
                if elevador >= 3:
                    print(f"O elevador {1} do tunel {tunel + 2} ira te levar ate o andar {proxima_posicao}")
                else:
                    print(f"O elevador {elevador + 1} do tunel {tunel + 1} ira te levar ate o andar {proxima_posicao}")
                floor_current = proxima_posicao
            
            elevador = elevador + 1
            if elevador >= 3:
                tunel = tunel + 1
                elevador = 0
        
        print("====================================================================================================")
        print(f"\n\nANDAR ATUAL: {floor_current}\nVOCE CHEGOU NO SEU ANDAR DE DESTINO!")
    
    else:
        position = [[25, 50, 75], [100, 125, 150], [175, 200, 225], [250, 275, 300]]
        while floor_current != floor_destiny:
            print("----------------------------------------------------------------------------------------------------")
            print(f"Andar atual: {floor_current}")
            if elevador == 0:
                if tunel == 0:
                    proxima_posicao = 1
                else:
                    proxima_posicao = position[tunel - 1][2]
            else:
                proxima_posicao = position[tunel][elevador - 1]
            
            if proxima_posicao < floor_destiny:
                floor_current = floor_destiny
            else:
                floor_current = proxima_posicao
            #print(proxima_posicao)
                
            if proxima_posicao != floor_destiny:
                print(f"O elevador {elevador + 1} do tunel {tunel  + 1} ira te levar ate o andar {proxima_posicao}")
            else:
                print(f"O elevador {elevador + 1} do tunel {tunel + 1} ira te levar ate ira te levar ate seu destino!")
                
                
            elevador = elevador - 1
            if elevador < 0:
                tunel = tunel - 1
                elevador = 2
            
        print("====================================================================================================")
        print(f"\n\nANDAR ATUAL: {floor_current}\nVOCE CHEGOU NO SEU ANDAR DE DESTINO!")  
            
    


print("\n\n=========================\n\tBEM VINDO!\n=========================\n")
main()
