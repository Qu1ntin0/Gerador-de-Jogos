import random
import os  

def gerar_combinacoes_com_sequencias(sequencias, total_numeros_por_combinacao, intervalo, combinacoes_por_sequencia):
    
    combinacoes = []
    
    for sequencia in sequencias:
        for _ in range(combinacoes_por_sequencia):
            numeros_restantes = total_numeros_por_combinacao - len(sequencia)
            if numeros_restantes < 0:
                raise ValueError("A sequência é longa demais para o total de números permitido na combinação.")
            
            numeros_aleatorios = random.sample(
                [n for n in intervalo if n not in sequencia], numeros_restantes
            )
            
            combinacao = sequencia + numeros_aleatorios
            random.shuffle(combinacao)  
            combinacoes.append(combinacao)
    
    return combinacoes

def salvar_combinacoes_em_arquivo(combinacoes, nome_arquivo):
    
    caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    caminho_arquivo = os.path.join(caminho_downloads, nome_arquivo)
    
    with open(caminho_arquivo, 'w') as arquivo:
        for i, combinacao in enumerate(combinacoes, start=1):
            linha = f"Combinação {i}: {combinacao}\n"
            arquivo.write(linha)
    print(f"As combinações foram salvas no arquivo: '{caminho_arquivo}'.")

def main():
    print("Gerador de combinações com sequências específicas/padrões e números aleatórios")
    
    sequencias = [
        [9, 10, 11],
        [13, 14, 15],
        [3, 4, 5],
        [5, 6, 7, 8],
        [16, 17, 18, 19],
        [21, 22, 23, 24, 25],
        [6, 7, 8],
        [15, 16, 17],
        [22, 23, 24],
        [8, 9, 10],
    ]
    total_numeros_por_combinacao = 15
    intervalo = range(1, 26)  
    combinacoes_por_sequencia = 2  
    
    try:
        combinacoes = gerar_combinacoes_com_sequencias(
            sequencias, total_numeros_por_combinacao, intervalo, combinacoes_por_sequencia
        )
        
        print(f"Foram geradas {len(combinacoes)} combinações únicas:\n")
        for i, combinacao in enumerate(combinacoes, start=1):
            print(f"Combinação {i}: {combinacao}")
        
        salvar_combinacoes_em_arquivo(combinacoes, "sequence.txt")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
