import random
import os 

def gerar_combinacoes_aleatorias(total_combinacoes, numeros_por_combinacao, intervalo):
 
    if numeros_por_combinacao > len(intervalo):
        raise ValueError("Não é possível gerar combinações com mais números do que o intervalo disponível.")
    
    combinacoes = set()
    while len(combinacoes) < total_combinacoes:
        combinacao = random.sample(intervalo, numeros_por_combinacao)  
        random.shuffle(combinacao) 
        combinacoes.add(tuple(combinacao)) 
    
    return list(combinacoes)

def salvar_combinacoes_em_arquivo(combinacoes, nome_arquivo):
    caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    caminho_arquivo = os.path.join(caminho_downloads, nome_arquivo)
    
    with open(caminho_arquivo, 'w') as arquivo:
        for i, combinacao in enumerate(combinacoes, start=1):
            linha = f"Combinação {i}: {combinacao}\n"
            arquivo.write(linha)
    print(f"As combinações foram salvas no arquivo: '{caminho_arquivo}'.")

def main():
    print("Gerador de 84 combinações aleatórias sem sequência numérica")
    
    total_combinacoes = 84
    numeros_por_combinacao = 15
    intervalo = range(1, 26) 
    nome_arquivo = "combinacoes.txt" 
    
    try:
        combinacoes = gerar_combinacoes_aleatorias(total_combinacoes, numeros_por_combinacao, intervalo)
        random.shuffle(combinacoes) 
        
        print(f"Foram geradas {len(combinacoes)} combinações únicas.\n")
        for i, combinacao in enumerate(combinacoes, start=1):
            print(f"Combinação {i}: {combinacao}")
        
        salvar_combinacoes_em_arquivo(combinacoes, nome_arquivo)
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
