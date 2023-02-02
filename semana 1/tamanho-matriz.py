#Função na qual é possivel saber a dimensão/tamanho de linhas e colunas de uma matriz
# Matriz definida pelo usuario no formato padrão. Ex.: matriz = [[1], [2], [3]]

def dimensoes(matriz):
    linhas = len(matriz) #lê o tamanho da linhas
    colunas = len(matriz[0]) #lê o tamanho das colunas
    
    print(f"{linhas}X{colunas}")
    
    #imprime no formato linhas X colunas 
