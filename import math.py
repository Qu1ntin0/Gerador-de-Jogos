import math

def calcular_combinacoes(x, r):
   
    if r > x:
        return 0  
    return math.comb(x, r)

def main():
    print("Programa para calcular combinações")
    
    try:
        x = int(input("Digite o tamanho do intervalo (x): "))
        r = int(input("Digite a quantidade de números para combinar (r): "))
        
        if x < 0 or r < 0:
            print("Os valores de x e r devem ser inteiros positivos.")
        else:
            resultado = calcular_combinacoes(x, r)
            print(f"O número de combinações possíveis é: {resultado}")
    
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

if __name__ == "__main__":
    main()

import random

def gerar_combinacoes_aleatorias(total_combinacoes, numeros_por_combinacao, intervalo):

    if numeros_por_combinacao > len(intervalo):
        raise ValueError("Não é possível gerar combinações com mais números do que o intervalo disponível.")
    
    combinacoes = set()
    while len(combinacoes) < total_combinacoes:
        combinacao = random.sample(intervalo, numeros_por_combinacao) 
        random.shuffle(combinacao) 
        combinacoes.add(tuple(combinacao))  
    
    return list(combinacoes)

def main():
    print("Gerador de 84 combinações aleatórias sem sequência numérica")
    
    total_combinacoes = 84
    numeros_por_combinacao = 15
    intervalo = range(1, 26) 
    
    try:
        combinacoes = gerar_combinacoes_aleatorias(total_combinacoes, numeros_por_combinacao, intervalo)
        random.shuffle(combinacoes)
        
        print(f"Foram geradas {len(combinacoes)} combinações únicas:\n")
        for i, combinacao in enumerate(combinacoes, start=1):
            print(f"Combinação {i}: {combinacao}")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
