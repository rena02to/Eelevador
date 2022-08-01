class Elevador:
    def __init__(self, nome, andar) -> None:
        self.nome = nome
        self.andar = andar
 
    def distance(self, andar):
        return abs(self.andar - andar)
 
class Tunel:
    def __init__(self, e1, e2, e3) -> None:
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
 
    def melhor_elevador(self, andar):
        d1 = self.e1.distance(andar)
        d2 = self.e2.distance(andar)
        d3 = self.e3.distance(andar)
        melhor = min(d1, d2, d3)
        if d1 == melhor:
            return d1, self.e1
        if d2 == melhor:
            return d2, self.e2
        if d3 == melhor:
            return d3, self.e3
 
    def get_elevador(self, andar):
        if self.e1.andar == andar:
            return self.e1
        if self.e2.andar == andar:
            return self.e2
        if self.e3.andar == andar:
            return self.e3
 
    def conflito(self, andar, e):
        if self.e1.andar == andar and self.e1.nome != e.nome:
            return True
        if self.e2.andar == andar and self.e2.nome != e.nome:
            return True
        if self.e3.andar == andar and self.e3.nome != e.nome:
            return True
 
        return False
 
    def resolver_conflito(self, andar, elevador):
        conflitado = self.get_elevador(andar)
        if elevador.andar < conflitado.andar:
            print(f"Subindo {conflitado.nome} de {conflitado.andar} até {conflitado.andar + 1} para evitar conflitos")
            conflitado.andar += 1
        else:
            print(f"Descendo {conflitado.nome} de {conflitado.andar} até {conflitado.andar - 1} para evitar conflitos")
            conflitado.andar -= 1
 
def melhor_tunel(andar, TUNEIS):
    i = 0
    melhor = 100000
    tunel = 5
    for i in range(4):
        d, e = TUNEIS[i].melhor_elevador(andar)
        if d < melhor:
            melhor = d
            tunel = i
    return d, tunel
 
def prioridade(req):
    d, tunel = melhor_tunel(req[0], TUNEIS)
    return d
 
def ler_opcao():
    print('Deseja apertar o botão do elevador?')
    print('[1] - SIM')
    print('[2] - NÃO')
    try:
        opt = int(input('Digite sua escolha: '))
        if opt == 1 or opt == 2:
            return opt
    except:
        print("Erro: Tente novamente")
 
    ler_opcao()
 
def ler_entrada():
    try:
        atual = int(input('Em qual piso você está?'))
        destino = int(input('Para qual piso você deseja ir?'))
        if atual > 300 or destino > 300 or atual < 1 or destino < 0:
            print("Erro: Tente novamente")
            ler_entrada()
        
        return (atual, destino)
    except:
        print("Erro: Tente novamente")
    ler_entrada()
 
def mover_elevador(req):
    andar = req[0]
    destino = req[1]
    d, tunel = melhor_tunel(andar, TUNEIS)
    t = TUNEIS[tunel]
    d, elevador = t.melhor_elevador(andar)
    if t.conflito(andar, elevador):
        t.resolver_conflito(andar, elevador)
 
    print(f"{elevador.nome} indo de {elevador.andar} para {andar} buscar um cliente")
    gasto = elevador.distance(andar)
    print(f"O Elevador mais próximo é o {elevador.nome}, com um distância de {gasto} andares, logo o tempo de espera e: {gasto}")
    elevador.andar = andar
    gasto += elevador.distance(destino)
    if t.conflito(destino, elevador):
        t.resolver_conflito(destino, elevador)
    print(f"{elevador.nome} indo de {elevador.andar} para {destino} deixar um cliente")
    elevador.andar = destino
    print(f"Gasto de energia: {gasto}")
 
if __name__ == '__main__':
    e1 = Elevador("Elevador A1", 1)
    e2 = Elevador("Elevador B1", 150)
    e3 = Elevador("Elevador C1", 300)
    t1 = Tunel(e1, e2, e3)
    e1 = Elevador("Elevador A2", 1)
    e2 = Elevador("Elevador B2", 150)
    e3 = Elevador("Elevador C2", 300)
    t2 = Tunel(e1, e2, e3)
    e1 = Elevador("Elevador A3", 1)
    e2 = Elevador("Elevador B3", 150)
    e3 = Elevador("Elevador C3", 300)
    t3 = Tunel(e1, e2, e3)
    e1 = Elevador("Elevador A4", 1)
    e2 = Elevador("Elevador B4", 150)
    e3 = Elevador("Elevador C4", 300)
    t4 = Tunel(e1, e2, e3)
 
    TUNEIS = [t1, t2, t3, t4]
 
    reqs = [] # Fila de prioridade
    while True:
        if ler_opcao() == 1:
            req = ler_entrada()
            reqs.append(req)
        else:
            break
 
    reqs.sort(key=prioridade)
 
    while len(reqs) > 0:
        primeiro_fila = reqs[0]
        mover_elevador(primeiro_fila)
        reqs = reqs[1:]
        reqs.sort(key=prioridade)
