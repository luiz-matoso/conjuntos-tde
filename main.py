##Instrucoes: Para mudar os valores dos conjuntos ou a ordem, voce deve alterar no arquivo dados.txt

def uni(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def inter(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def dif(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def cart(conjunto1, conjunto2):
    return {(x, y) for x in conjunto1 for y in conjunto2}


def executar(operacao, conjunto1, conjunto2):
    if operacao == 'U':
        return uni(conjunto1, conjunto2)

    elif operacao == 'I':
        return inter(conjunto1, conjunto2) 

    elif operacao == 'D':
        return dif(conjunto1, conjunto2)

    elif operacao == 'C':
        return cart(conjunto1, conjunto2)

               
def ler_arquivo(dados_txt):
    operacoes = []
    with open(dados_txt, 'r') as dados:
        n_operacoes = int(dados.readline().strip())
        for _ in range(n_operacoes):
            operacao = dados.readline().strip()
            conjunto1 = set(dados.readline().strip().split(','))
            conjunto2 = set(dados.readline().strip().split(','))
            operacoes.append((operacao, conjunto1, conjunto2))
    return operacoes

def main():
    dados_txt = 'dados.txt'
    operacoes = ler_arquivo(dados_txt)
    for operacao, conjunto1, conjunto2, in operacoes:
        resultado = executar(operacao, conjunto1, conjunto2)
        
        print(f'Operacao: {operacao}, Resultado: {resultado}')

if __name__ == "__main__":
    main()        

